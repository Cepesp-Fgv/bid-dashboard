let mix = require('laravel-mix');

mix
    .js('resources/js/dashboard.js', 'js')
    .sass('resources/sass/app.scss', 'css')
    .setPublicPath('static')
    .browserSync('localhost:5000');