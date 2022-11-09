import {describe} from '@jest/globals';
import {rpn} from "../src/functions";

describe("rpn", () => {
    test("should return the correct result", () => {
        expect(rpn("2 2 +")).toBe(4);
    });
})