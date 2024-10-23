import { test, expect } from '@playwright/test';

test('should have the correct HTML title', async ({ page }) => {
    await page.goto('http://localhost:5173/');
    await expect(page).toHaveTitle('Employee');
});

test('should have the correct H1 text', async ({ page }) => {
    await page.goto('http://localhost:5173/');
    await expect(page.locator('h1')).toHaveText('Hello from React.js!');
});
