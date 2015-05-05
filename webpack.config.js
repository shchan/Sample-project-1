var webpack = require('webpack');
var bower_dir = __dirname + '/bower_components';

var config = {
    addVendor: function (name, path) {
        this.resolve.alias[name] = path;
        this.module.noParse.push(new RegExp(path));
    },
    entry: {
        app: ["./entry.js"],
        vendors: [
            'jquery',
            'react',
        ],
    },
    resolve: { alias: {} },
    plugins: [
        new webpack.optimize.CommonsChunkPlugin('vendors', 'vendors.js')
    ],
    output: {
        path: "./static",
        filename: "bundle.js"
    },
    module: {
        noParse: [bower_dir + '/react/react.min.js'],
        loaders: [
            { test: /\.css$/, loader: 'style-loader!css-loader' },
            { test: /\.js$/, loader: 'jsx-loader' },
            { test: /\.png$/, loader: 'url-loader?limit=100000' },
            { test: /\.woff2?$/,loader: "url-loader?limit=10000&minetype=application/font-woff" },
            { test: /\.ttf$/, loader: "file-loader" },
            { test: /\.eot$/, loader: "file-loader" },
            { test: /\.svg$/, loader: "file-loader" }
        ]
    }
};

config.addVendor('jquery', bower_dir + '/jquery/dist/jquery.min.js');
config.addVendor('react', bower_dir + '/react/react.min.js');
// config.addVendor('bootstrap-datepicker', bower_dir + '/bootstrap-3-datepicker/dist/js/bootstrap-datepicker.min.js')
// config.addVendor('bootstrap-datepicker.css', bower_dir + '/bootstrap-3-datepicker/dist/css/bootstrap-datepicker3.min.css')

module.exports = config;
