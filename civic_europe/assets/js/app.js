/* global location */

const widget = require('adhocracy4').widget
const ReactComments = require('adhocracy4').comments
const ReactFollow = require('../../../apps/follows/static/follows/react_follows.jsx')
const ReactSupport = require('../../../apps/ideas/static/civic_europe_ideas/react_supports.jsx')
const $ = window.jQuery = window.$ = require('jquery')

// load bootstrap components
require('bootstrap')

require('../../../civic_europe/assets/js/civic_europe')

$(function () {
  widget.initialise('a4', 'comment', ReactComments.renderComment)
  widget.initialise('ae', 'follows', ReactFollow.renderFollow)
  widget.initialise('ae', 'supports', ReactSupport.renderSupports)
  // changing bs5 elements to bs4 in civic europe
  require('../../../civic_europe/assets/js/bootstrap5-fix')
})

const getCurrentPath = function () {
  return location.pathname
}

module.exports = {
  getCurrentPath: getCurrentPath
}
