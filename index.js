function sleep(ms) {
    const wakeUpTime = Date.now() + ms;
    while (Date.now() < wakeUpTime) {}
}

console.log("그거 아시나요?")
sleep(1000);
console.log("인생은 하나라는거")
sleep(1000);
console.log("하나이기에")
sleep(300)
console.log("재밌게 살아야하는게");
sleep(100);
console.log("아닐까요?");
sleep(1000);
console.log("저 역시 질문하고 싶군요");
sleep(500);
console.log("이걸 보고계신 선생님은");
sleep(1000);
console.log("행복하신가요?");