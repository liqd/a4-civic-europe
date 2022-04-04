document.addEventListener('DOMContentLoaded', function() {
  const videoEmbeds = document.querySelectorAll('.rich-text iframe')

  for (const videoEmbed of videoEmbeds) {
    const parentOfEmbed = videoEmbed.parentElement
    // following classnames are bs4 classnames
    parentOfEmbed.classList.add('embed-responsive')
    parentOfEmbed.classList.add('embed-responsive-16by9')
  }
})
