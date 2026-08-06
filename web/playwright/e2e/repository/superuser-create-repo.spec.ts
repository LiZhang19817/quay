import {test, expect} from '../../fixtures';

test.describe(
  'Superuser namespace search in Create Repository',
  {tag: ['@superuser', '@feature:SUPERUSERS_FULL_ACCESS']},
  () => {
    test('superuser with full access sees namespace selector in create repo modal', async ({
      superuserPage,
    }) => {
      await superuserPage.goto('/repository');

      await superuserPage
        .getByRole('button', {name: 'Create Repository'})
        .click();

      const dropdown = superuserPage.getByTestId('selected-namespace-dropdown');
      await expect(dropdown).toBeVisible();
    });
  },
);
