/**
 * Google Sheets Integration Configuration
 * ----------------------------------------------------
 * 1. Google Sheet 공유 설정: "링크가 있는 모든 사용자에게 공개(읽기 가능)" 로 설정합니다.
 * 2. 구글 시트 URL에서 SPREADSHEET_ID를 복사하여 아래 변수에 입력합니다.
 *    예: https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit -> "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"
 * 
 * 구글 시트 헤더(1행) 추천 열 이름:
 * title | category | description | tech_stack | date | link | demo_link
 */
const SPREADSHEET_ID = ""; // 구글 시트 ID를 입력하세요.

// 기본 샘플 데이터 (구글 시트 ID가 비어있거나 불러오기 실패 시 출력)
const SAMPLE_PROJECTS = [
    {
        title: "Distributed LLM Inference Pipeline",
        category: "ML/DL",
        description: "PyTorch 및 vLLM 기반 대규모 언어 모델 서빙 및 분산 추론 최적화 파이프라인. TensorRT-LLM과 Triton Inference Server를 도입하여 처리량 3배 향상.",
        tech_stack: "Python, PyTorch, vLLM, Docker, FastAPI",
        date: "2024.05",
        link: "https://github.com",
        demo_link: ""
    },
    {
        title: "High-Throughput Event Streaming Infrastructure",
        category: "Backend",
        description: "Kafka 및 Go 기반 초당 50k+ 건의 이벤트를 유실 없이 분산 처리하는 메시지 스트리밍 인프라 구축.",
        tech_stack: "Go, Apache Kafka, Redis, PostgreSQL, Kubernetes",
        date: "2024.02",
        link: "https://github.com",
        demo_link: ""
    },
    {
        title: "Multimodal Medical Image Segmentation Engine",
        category: "ML/DL",
        description: "3D Brain MRI 데이터를 위한 UNet3D 기반 병변 자동 분할 딥러닝 모델 개발 및 MONAI 프레임워크 전처리 자동화.",
        tech_stack: "Python, PyTorch, CUDA, MONAI, Weights & Biases",
        date: "2023.11",
        link: "https://github.com",
        demo_link: "https://scholar.google.com"
    },
    {
        title: "Async Task Scheduler & Worker Engine",
        category: "Backend",
        description: "지연 실행, 지수 백오프 재시도, 실패 큐 모니터링을 지원하는 분산 작업 큐 시스템 개발.",
        tech_stack: "Python, Redis, Celery, FastAPI, Prometheus",
        date: "2023.08",
        link: "https://github.com",
        demo_link: ""
    }
];

let allProjects = [];
let activeCategory = "All";
let searchQuery = "";

document.addEventListener("DOMContentLoaded", () => {
    initPortfolio();
});

async function initPortfolio() {
    const noticeEl = document.getElementById("SheetNotice");
    
    if (SPREADSHEET_ID && SPREADSHEET_ID.trim() !== "") {
        try {
            renderLoadingState();
            allProjects = await fetchGoogleSheetProjects(SPREADSHEET_ID.trim());
            if (noticeEl) noticeEl.style.display = "none";
        } catch (err) {
            console.warn("Google Sheets 데이터 로드 실패. 샘플 데이터로 전환합니다:", err);
            allProjects = SAMPLE_PROJECTS;
            if (noticeEl) {
                noticeEl.style.display = "block";
                noticeEl.innerHTML = `⚠️ 구글 시트 데이터를 가져올 수 없어 샘플 데이터를 표시 중입니다. (시트 공개 권한을 확인하세요)`;
            }
        }
    } else {
        allProjects = SAMPLE_PROJECTS;
        if (noticeEl) noticeEl.style.display = "block";
    }

    setupCategoryFilters();
    setupSearchInput();
    renderProjects();
}

/**
 * 구글 시트 CSV 데이터 Fetch 및 파싱
 */
async function fetchGoogleSheetProjects(sheetId) {
    const url = `https://docs.google.com/spreadsheets/d/${sheetId}/gviz/tq?tqx=out:csv`;
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error(`HTTP Error ${response.status}`);
    }
    const csvText = await response.text();
    return parseCSV(csvText);
}

/**
 * 쉼표 및 큰따옴표를 처리하는 RFC4180 호환 간단 CSV 파서
 */
function parseCSV(text) {
    const lines = [];
    let row = [];
    let inQuotes = false;
    let currentToken = '';

    for (let i = 0; i < text.length; i++) {
        const char = text[i];
        const nextChar = text[i + 1];

        if (char === '"') {
            if (inQuotes && nextChar === '"') {
                currentToken += '"';
                i++;
            } else {
                inQuotes = !inQuotes;
            }
        } else if (char === ',' && !inQuotes) {
            row.push(currentToken.trim());
            currentToken = '';
        } else if ((char === '\r' || char === '\n') && !inQuotes) {
            if (char === '\r' && nextChar === '\n') i++;
            row.push(currentToken.trim());
            if (row.some(field => field.length > 0)) {
                lines.push(row);
            }
            row = [];
            currentToken = '';
        } else {
            currentToken += char;
        }
    }
    if (currentToken || row.length > 0) {
        row.push(currentToken.trim());
        if (row.some(field => field.length > 0)) {
            lines.push(row);
        }
    }

    if (lines.length < 2) return [];

    const headers = lines[0].map(h => h.toLowerCase().replace(/\s+/g, '_'));
    const data = [];

    for (let i = 1; i < lines.length; i++) {
        const values = lines[i];
        const item = {};
        headers.forEach((header, idx) => {
            item[header] = values[idx] || '';
        });
        data.push(item);
    }

    return data;
}

/**
 * 카테고리 필터 버튼 생성 및 이벤트 바인딩
 */
function setupCategoryFilters() {
    const container = document.getElementById("CategoryFilters");
    if (!container) return;

    const categories = ["All", ...new Set(allProjects.map(p => p.category).filter(Boolean))];

    container.innerHTML = categories.map(cat => `
        <button class="Filter-Btn ${cat === activeCategory ? 'active' : ''}" data-category="${cat}">
            ${cat}
        </button>
    `).join('');

    container.addEventListener("click", (e) => {
        const btn = e.target.closest(".Filter-Btn");
        if (!btn) return;
        
        activeCategory = btn.dataset.category;
        document.querySelectorAll(".Filter-Btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        renderProjects();
    });
}

/**
 * 검색 입력 이벤트 바인딩
 */
function setupSearchInput() {
    const input = document.getElementById("SearchInput");
    if (!input) return;

    input.addEventListener("input", (e) => {
        searchQuery = e.target.value.toLowerCase().trim();
        renderProjects();
    });
}

/**
 * 프로젝트 그리드 렌더링
 */
function renderProjects() {
    const grid = document.getElementById("ProjectsGrid");
    if (!grid) return;

    const filtered = allProjects.filter(p => {
        const matchCategory = activeCategory === "All" || p.category === activeCategory;
        const searchTarget = `${p.title || ''} ${p.description || ''} ${p.tech_stack || ''} ${p.category || ''}`.toLowerCase();
        const matchSearch = !searchQuery || searchTarget.includes(searchQuery);
        return matchCategory && matchSearch;
    });

    if (filtered.length === 0) {
        grid.innerHTML = `
            <div class="Empty-State">
                <p>검색 조건에 맞는 프로젝트가 없습니다.</p>
            </div>
        `;
        return;
    }

    grid.innerHTML = filtered.map(p => createProjectCardHTML(p)).join('');
}

function renderLoadingState() {
    const grid = document.getElementById("ProjectsGrid");
    if (grid) {
        grid.innerHTML = `
            <div class="Loading-State">
                <div class="Spinner"></div>
                <p>Google Sheets 프로젝트 불러오는 중...</p>
            </div>
        `;
    }
}

/**
 * 개별 프로젝트 카드 HTML 생성을 담당
 */
function createProjectCardHTML(p) {
    const techStack = p.tech_stack 
        ? p.tech_stack.split(',').map(s => `<span class="Tech-Badge">${escapeHTML(s.trim())}</span>`).join('')
        : '';

    const primaryLink = p.link 
        ? `<a href="${escapeHTML(p.link)}" target="_blank" rel="noopener noreferrer" class="Card-Link Primary-Link">GitHub / Repo ↗</a>`
        : '';
        
    const demoLink = p.demo_link 
        ? `<a href="${escapeHTML(p.demo_link)}" target="_blank" rel="noopener noreferrer" class="Card-Link Secondary-Link">Demo / Paper ↗</a>`
        : '';

    return `
        <article class="Project-Card">
            <div class="Card-Header">
                <span class="Category-Badge">${escapeHTML(p.category || 'Project')}</span>
                ${p.date ? `<span class="Project-Date">${escapeHTML(p.date)}</span>` : ''}
            </div>
            <h3 class="Project-Title">${escapeHTML(p.title || 'Untitled Project')}</h3>
            <p class="Project-Desc">${escapeHTML(p.description || '')}</p>
            ${techStack ? `<div class="Tech-Stack">${techStack}</div>` : ''}
            <div class="Card-Footer">
                ${primaryLink}
                ${demoLink}
            </div>
        </article>
    `;
}

function escapeHTML(str) {
    return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}
