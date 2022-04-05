// This file runs on every load and checks if there are any bootstrap 5
// data attributes on any DOM elements. It checks for data-bs-toggle,
// data-bs-dismiss and data-bs-target attributes and converts them to
// bootstrap 4 equivalent attributes.

const bs5ToggleElements =
  document.querySelectorAll('[data-bs-toggle]')

for (const toggleEl of bs5ToggleElements) {
  const value = toggleEl.getAttribute('data-bs-toggle')
  if (value) {
    toggleEl.setAttribute('data-toggle', value)
    toggleEl.removeAttribute('data-bs-toggle')
  }
}

const bs5DismissElements =
  document.querySelectorAll('[data-bs-dismiss]')

for (const dismissEl of bs5DismissElements) {
  const value = dismissEl.getAttribute('data-bs-dismiss')
  if (value) {
    dismissEl.setAttribute('data-dismiss', value)
    dismissEl.removeAttribute('data-bs-dismiss')
  }
}

const bs5TargetElements =
  document.querySelectorAll('[data-bs-target]')

for (const targetEl of bs5TargetElements) {
  const value = targetEl.getAttribute('data-bs-target')
  if (value) {
    targetEl.setAttribute('data-target', value)
    targetEl.removeAttribute('data-bs-target')
  }
}
