document.addEventListener('DOMContentLoaded', function () {
  const iframeSelectors = [
    '.rich-text iframe',
    '.block-qa iframe',
    '.block-col-1 iframe',
    '.block-col-2 iframe',
    '.block-col-3 iframe'
  ]

  const videoEmbeds = document.querySelectorAll(iframeSelectors.join(', '))

  for (const videoEmbed of videoEmbeds) {
    const parentOfEmbed = videoEmbed.parentElement
    // following classnames are bs4 classnames
    parentOfEmbed.classList.add('embed-responsive')
    parentOfEmbed.classList.add('embed-responsive-16by9')
  }
})
