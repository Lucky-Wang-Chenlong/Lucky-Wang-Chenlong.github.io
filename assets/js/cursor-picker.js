(function () {
  'use strict';

  const picker = document.querySelector('.cursor-picker');
  if (!picker) return;

  const choices = Array.from(picker.querySelectorAll('input[name="bird-cursor"]'));
  const caption = document.getElementById('cursorName');
  const storageKey = 'bird-cursor';
  const root = document.documentElement;
  const hotspots = {
    cockatoo: [4, 13],
    cockatiel: [5, 12],
    toucan: [2, 9],
    lovebird: [5, 10]
  };
  const pointer = document.createElement('img');
  pointer.className = 'bird-pointer';
  pointer.alt = '';
  pointer.setAttribute('aria-hidden', 'true');
  pointer.width = 32;
  pointer.height = 32;
  pointer.draggable = false;
  pointer.hidden = true;
  document.body.appendChild(pointer);

  let position = null;
  let hotspot = hotspots.cockatoo;

  function hidePointer() {
    position = null;
    pointer.hidden = true;
    root.removeAttribute('data-bird-pointer');
  }

  function renderPointer() {
    if (!position || !pointer.complete || !pointer.naturalWidth) return;
    pointer.style.transform = 'translate3d(' + (position.x - hotspot[0]) + 'px, ' +
      (position.y - hotspot[1]) + 'px, 0)';
    pointer.hidden = false;
    root.setAttribute('data-bird-pointer', 'visible');
  }

  pointer.addEventListener('load', renderPointer);
  pointer.addEventListener('error', hidePointer);

  document.addEventListener('pointermove', function (event) {
    if (event.pointerType !== 'mouse') {
      hidePointer();
      return;
    }
    position = { x: event.clientX, y: event.clientY };
    renderPointer();
  }, { passive: true });
  document.addEventListener('pointerdown', function (event) {
    if (event.pointerType !== 'mouse') hidePointer();
  }, { passive: true });
  root.addEventListener('pointerleave', hidePointer);
  window.addEventListener('blur', hidePointer);
  document.addEventListener('visibilitychange', function () {
    if (document.hidden) hidePointer();
  });

  function selectCursor(value) {
    const selected = choices.find(function (choice) {
      return choice.value === value;
    }) || choices[0];

    selected.checked = true;
    root.dataset.cursor = selected.value;
    hotspot = hotspots[selected.value];
    // Load from the same image the picker displays, avoiding CSS URL ambiguity.
    pointer.hidden = true;
    root.removeAttribute('data-bird-pointer');
    pointer.src = selected.closest('label').querySelector('img').src;
    renderPointer();
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
