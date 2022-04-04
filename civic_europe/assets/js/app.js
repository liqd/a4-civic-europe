/* global location */

const widget = require('adhocracy4').widget
const ReactComments = require('adhocracy4').comments
const ReactFollow = require('../../../apps/follows/static/follows/react_follows.jsx')
const ReactSupport = require('../../../apps/ideas/static/civic_europe_ideas/react_supports.jsx')
const $ = window.jQuery = window.$ = require('jquery')

// load bootstrap components
require('bootstrap')

require('../../../civic_europe/assets/js/civic_europe')
require('../../../civic_europe/assets/js/wagtail-videoembed-fix')

$(function () {
  widget.initialise('a4', 'comment', ReactComments.renderComment)
  widget.initialise('ae', 'follows', ReactFollow.renderFollow)
  widget.initialise('ae', 'supports', ReactSupport.renderSupports)
})

const getCurrentPath = function () {
  return location.pathname
}

module.exports = {
  getCurrentPath: getCurrentPath
}
