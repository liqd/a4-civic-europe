/* global location */

var widget = require('adhocracy4').widget
var ReactComments = require('adhocracy4').comments
var ReactCommentsAsync = require('adhocracy4').comments_async
var ReactFollow = require('../../../apps/follows/static/follows/react_follows.jsx')
var ReactSupport = require('../../../apps/ideas/static/civic_europe_ideas/react_supports.jsx')
var $ = window.jQuery = window.$ = require('jquery')

// load bootstrap components
require('bootstrap')

require('../../../civic_europe/assets/js/civic_europe')

$(function () {
  widget.initialise('a4', 'comment', ReactComments.renderComment)
  widget.initialise('a4', 'comment_async', ReactCommentsAsync.renderComment)
  widget.initialise('ae', 'follows', ReactFollow.renderFollow)
  widget.initialise('ae', 'supports', ReactSupport.renderSupports)
})

var getCurrentPath = function () {
  return location.pathname
}

module.exports = {
  getCurrentPath: getCurrentPath
}
