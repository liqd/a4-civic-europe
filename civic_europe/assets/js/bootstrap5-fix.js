const bs5ToggleElements =
  document.querySelectorAll('*[data-bs-toggle]')

for (const toggleEl of bs5ToggleElements) {
  if (toggleEl.dataset.bsToggle) {
    toggleEl.dataset.toggle = toggleEl.dataset.bsToggle
    delete toggleEl.dataset.bsToggle
  }
}

const bs5DismissElements =
  document.querySelectorAll('*[data-bs-dismiss]')

for (const dismissEl of bs5DismissElements) {
  if (dismissEl.dataset.bsDismiss) {
    dismissEl.dataset.dismiss = dismissEl.dataset.bsDismiss
    delete dismissEl.dataset.bsDismiss
  }
}

const bs5TargetElements =
  document.querySelectorAll('*[data-bs-target]')

for (const targetEl of bs5TargetElements) {
  if (targetEl.dataset.bsTarget) {
    targetEl.dataset.target = targetEl.dataset.bsTarget
    delete targetEl.dataset.bsTarget
  }
}
