module.exports = {
    devServer: {
	hot: true,
    liveReload: false,
        proxy: 'http://172.20.10.2:3000'
    },
    css: { extract: false },
    assetsDir: 'static',
    configureWebpack:{
        devtool: 'source-map',
        optimization: {
          splitChunks: {
            minSize: 10000,
            maxSize: 250000,
          }
        }
      },
      productionSourceMap: true, // NOTE: this is default

}
