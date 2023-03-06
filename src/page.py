class pages:
    def description(description:str, author:str) -> str:
        return f"""
        <meta name="description" content={description} />
        <meta name="author" content={author} /> 
        
        <meta property="og:type" content="website">
        <meta property="og:title" content={author}>
        <meta property="og:description" content={description}>

        """
        
        
    def titlediv(signature_color:str, name:str, email:str, URL:dict) -> str:
        urlhtml = ""
        for url in URL:
            urlhtml += f"""
                <a href="{URL[url]}">{url} /> |
            """

        return f"""
            <div class="wrap" align="middle">
                <div style="background-color: #000;">
                    <div class="background" style="background-color: {signature_color};"></div>
                </div>
                
                <div class="text">
                    <h1 class="name">{name}</h1>
                    <h4 class="copyright">| 
                        <a href="mailto:{email}">Email</a>  | 
                        {urlhtml}
                    </h4>
                </div>
            </div>

            """
        

    def introduction(abouts:dict) -> str:
        abouthtml = ""
        for about in abouts:
            abouthtml += f"<p>{about}</p>\n"

        return f"""
            <!-- Introduction -->
            <section id="about" class="main">
                <div class="spotlight">
                    <div class="content">
                        <header class="major">
                            <h2>About me</h2>
                        </header>
                        {abouthtml}
                    </div>
                </div>
            </section>

            """
        

    def firstsection(langs:dict) -> str:
        frameworkhtml = ""
        for lang in langs.items():
            langlist = ""
            for framework in lang[1]['framework']:
                frameworkhtml += f"""<h4 class="skill-detail">{framework}</h4>\n"""
            
            langlist += f"""
                <li>
                    <i class="{lang[0]}" style="color: {lang[1]['color']};"></i>
                    <h3 class='skill-name'>{lang[1]['name']}</h3>
                    {frameworkhtml}
                </li>

            """

        return f"""
            <!-- First Section -->
            <section id="skill" class="main special">
                <header class="major">
                    <h2>Skill</h2>
                </header>
                <ul class="features">
                    {langlist}
                </ul>
            </section>

            """
        

    def secondsection(projects:dict, github:str) -> str:
        projecthtml = ""
        for name in projects.items():
            urlhtml = ""
            if name[1]['url']:
                urlhtml += """
                <a href="https://{{name[1]['url']}}">
                    <i class="fa-solid fa-globe fa-2x" style="margin-bottom: 20px; margin-top: 9px;" aria-hidden="true"></i>
                </a>
                """

            projecthtml += f"""
                <li>
                    <div class="card">
                        <i class="fab fa-{name[1]['lang']} fa-4x" style="color: {name[1]['color']}; margin-top: 20px;"></i>
                        <h3 class="project-name">{name[0]}</h3>
                        <h4 class="project-detail">{name[1]['info_text']}</h4>
                        <div>
                            <a href="{name[1]['github']}">
                                <i class="fab fa-github fa-2x" style="margin-bottom: 20px; margin-top: 9px;" aria-hidden="true"></i>
                            </a>
                            {urlhtml}
                        </div>						
                    </div>
                </li>

                """

        return f"""
            <!-- Second Section -->
            <section id="project" class="main special">
                <header class="major">
                    <h2>Project</h2>
                </header>
                <!-- <pre class="project_info"></pre> -->
                <ul class="features">
                    {projecthtml}
                </ul>
                <footer class="major">
                    <ul class="actions special">
                        <li><a href="{github}" class="button">More on Github</a></li>
                    </ul>
                </footer>
            </section>

            """
        

    def introduction_two(career:dict) -> str:
        carrerloadhtml = ""
        for career in career.items():
            careerhtml = ""
            for career in career[1]:
                careerhtml += f"""
                    <p><pre>{career}</pre></p>
                """
        
            carrerloadhtml += f"""
                <div>
                    <h3>{career[0]}</h3>
                    {careerhtml}
                </div>

            """
        
        return f"""
            <!-- Introduction -->
            <section id="career" class="main">
                <!-- special -->
                <div class="spotlight">
                    <div class="content">
                        <header class="major">
                            <h2>Career</h2>
                        </header>
                        {carrerloadhtml}
                    </div>
                </div>
            </section>

            """
        
    
    def getstarted(email:str, github:str, urllists:dict) -> str:
        urlhtml = ""
        for url in urllists:
            urlhtml += f"""
            <p>{url} : <a href="{urllists[url]}" target="_top">{urllists[url]}</a></p>
            """

        return f"""
            <!-- Get Started -->
            <section id="contact" class="main special">
                <header class="major">
                    <h2>Contact</h2>
                </header>
                <p>Email : <a href="mailto:{email}" target="_top">{email}</a></p>
                {urlhtml}
                </br></br>
                <h4 class="copyright">
                    <a href="{github}/portfolio-webpages">Copyrightⓒ2022 by Mireu Lim</a>
                </h4>
            </section>

            """
        
        

    def save(
        description:str, 
        titlediv:str, 
        introduction:str, 
        firstsection:str, 
        secondsection:str, 
        introduction_two:str,
        getstarted:str) -> bool:

        setpage = f"""
            <html>
            <head>
                <meta charset="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
                
                {description}

                <link rel="stylesheet" href="css/style.css" />
                <script src="https://kit.fontawesome.com/5a354dca55.js" crossorigin="anonymous"></script>
            </head>

            <body class="is-preload" style="margin:0; padding:0">
                <!-- Wrapper -->
                <div id="wrapper">

                    <!-- Main -->
                    <div id="main">
                        {titlediv}
                        {introduction}
                        {firstsection}
                        {secondsection}
                        {introduction_two}
                        {getstarted}
                    </div>
                </div>

                <!-- Scripts -->
                <script src="js/jquery.min.js"></script>
                <script src="js/jquery.scrollex.min.js"></script>
                <script src="js/jquery.scrolly.min.js"></script>
                <script src="js/browser.min.js"></script>
                <script src="js/breakpoints.min.js"></script>
                <script src="js/util.js"></script>
                <script src="js/main.js"></script>

            </body>
            </html>
            """
        
        try:
            with open("./page/index.html", "w") as indexhtml:
                indexhtml.write(setpage)

            return True
        
        except:
            return False
