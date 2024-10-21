import { test, expect } from 'vitest'

let testString = 'test string';

test('test string', () => {
    expect('test string').toBe(testString)
});
