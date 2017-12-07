var webpack = require('webpack');
var path = require('path');

var BUILD_DIR = path.resolve(__dirname, 'src/client/public'); // Directory path of the bundle file output
var APP_DIR = path.resolve(__dirname, 'src/client/app'); // Directory path of react application

var config = {
  entry: APP_DIR + '/index.jsx',
  output: {
    path: BUILD_DIR,
    filename: 'bundle.js'
  },
  /**
   * This syntax can be confusing (fortunately it’s not something we’ll
   * be editing often). Basically we’re telling webpack to look for any .js
   * files (excluding ones in the node_modules folder) and apply babel transpilation
   * using babel-loader with the babel-preset-env preset. You can read more about
   * webpack configuration syntax here.
   */
  module: {
    loaders: [
      // {
      //   test: /\.js$/,
      //   loader: 'babel-loader',
      //   include : APP_DIR,
      //   exclude: /node_modules/
      // },
      {
        test: /\.jsx$/,
        loader: 'babel-loader',
        include : APP_DIR,
        exclude: /node_modules/ }
    ]
  }
}


module.exports = config;
