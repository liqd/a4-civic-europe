var MiniCssExtractPlugin = require('mini-css-extract-plugin')
var CopyWebpackPlugin = require('copy-webpack-plugin')
var path = require('path')
var webpack = require('webpack');
var autoprefixer = require('autoprefixer');


/** How do we use webpack to handle static files?
 *
 * - dependencies (js, scss, and css) are installed via npm
 * - dependencies (js, scss, and css ) are moved to `vendor.(js|css)`
 *   by specifing them in the vendor entry point
 * - everything else (our js, scss) is compiled into app.(js|css)
 * - our images, fonts, icons, js, css and scss is either in each apps
 *   static folder (/euth/<appname>/static) or in the projects asset folder
 *   (/euth_wagtail/assets)
 * - after running webpack all static ressources will be in the
 *   project static folder (/euth_wagtail/static) and can then be served
 *   by django
 * - webpack compiles jsx+es2015 to js and scss to css for us
 */

module.exports = {
  entry: {
    adhocracy4: [
      './civic_europe/assets/scss/all.scss',
      './civic_europe/assets/js/app.js'
    ],
    vendor: [
      'jquery',
      'react',
      'react-dom',
      'react-addons-update',
      'classnames',
      '@fortawesome/fontawesome-free/scss/fontawesome.scss',
      '@fortawesome/fontawesome-free/scss/brands.scss',
      '@fortawesome/fontawesome-free/scss/regular.scss',
      '@fortawesome/fontawesome-free/scss/solid.scss',
      './civic_europe/assets/js/jquery-fix.js',
      'slick-carousel/slick/slick.min.js',
      'slick-carousel/slick/slick.css'
    ],
    image_uploader: [
        'adhocracy4/adhocracy4/images/assets/image_uploader.js'
    ]
  },
  output: {
    library: {
      name: '[name]',
      type: 'var'
    },
    path: path.resolve('./civic_europe/static/'),
    publicPath: '/static/',
    filename: '[name].js'
  },
  externals: {
    django: 'django'
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules\/(?!(adhocracy4|bootstrap)\/).*/,  // exclude all dependencies but adhocracy4
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react'].map(require.resolve),
            plugins: ['@babel/plugin-transform-runtime', '@babel/plugin-transform-modules-commonjs']
          }
        }
      },
      {
        test: /\.s?css$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader
          },
          {
            loader: 'css-loader'
          },
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: [
                  require('autoprefixer')
                ]
              }
            }
          },
          {
            loader: 'sass-loader',
            options: {
              sassOptions: {
                includePaths: [
                  path.resolve('./node_modules/bootstrap-sass/assets/stylesheets')
                ]
              }
            }
          }
        ]
      },
      {
        test: /fonts\/.*\.(svg|woff2?|ttf|eot)(\?.*)?$/,
        // defines asset should always have seperate file
        type: 'asset/resource',
        generator: {
          // defines custom location of those files
          filename: 'fonts/[name][ext]'
        }
      },
      {
        test: /\.svg$|\.png$/,
        type: 'asset/resource',
        generator: {
          filename: 'images/[name][ext]'
        }
      }
    ]
  },
  resolve: {
    extensions: ['*', '.js', '.jsx', '.scss', '.css'],
    // when using `npm link`, dependencies are resolved against the linked
    // folder by default. This may result in dependencies being included twice.
    // Setting `resolve.root` forces webpack to resolve all dependencies
    // against the local directory.
    modules: [path.resolve('./node_modules')]
  },
  plugins: [
    new webpack.optimize.SplitChunksPlugin({ name: 'vendor', filename: 'vendor.js'}),
    new MiniCssExtractPlugin({
      filename: '[name].css',
      chunkFilename: '[id].css'
    }),
    new CopyWebpackPlugin({
      patterns: [
        {
          from: './civic_europe/assets/images/**/*',
          to: 'images/[name][ext]'
        },
        {
          from: './civic_europe/assets/icons/**/*',
          to: 'icons/[name][ext]'
         }
    ]})
  ]
}
