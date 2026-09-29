(function () {
  'use strict';

  const picker = document.querySelector('.cursor-picker');
  if (!picker) return;

  const choices = Array.from(picker.querySelectorAll('input[name="bird-cursor"]'));
  const caption = document.getElementById('cursorName');
  const storageKey = 'bird-cursor';

  function selectCursor(value) {
    const selected = choices.find(function (choice) {
      return choice.value === value;
    }) || choices[0];

    selected.checked = true;
    document.documentElement.dataset.cursor = selected.value;
    caption.textContent = selected.dataset.name;
    return selected.value;
  }

  let savedCursor;
  try {
    savedCursor = localStorage.getItem(storageKey);
  } catch (_) {
    // Cursor switching also works when browser storage is unavailable.
  }
  selectCursor(savedCursor);
  picker.hidden = false;

  picker.addEventListener('change', function (event) {
    if (!choices.includes(event.target)) return;
    const value = selectCursor(event.target.value);
    try {
      localStorage.setItem(storageKey, value);
    } catch (_) {
      // Keep the choice active for this page even if it cannot be saved.
    }
  });
})();
