var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
context: __dirname,

entry: './reactComs/js/index.js', 

output: {
    path: path.resolve('./reactComs/bundles/'),
    filename: "[name]-[hash].js",
},

plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
],

module: {
    loaders: [
    { test: /\.js$/, loader: 'babel-loader', exclude: /node_modules/ },
    { test: /\.jsx$/, loader: 'babel-loader', exclude: /node_modules/ }

    ],
},

}