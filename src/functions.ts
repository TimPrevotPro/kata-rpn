export function rpn(args: string): number {
    const splittedArgs = args.split(" ");
    const numbers: number[] = [];
    splittedArgs.forEach((arg) => {
        if (!isNaN(parseInt(arg))) {
            numbers.push(parseInt(arg));
        } else if (arg === "+") {
            let res = numbers[0] + numbers[1];
            numbers.pop();
            numbers.pop()
            numbers.push(res);
        } else {
            console.error("fail");
        }
    });
    return numbers[0];
}