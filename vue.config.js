module.exports = {
    devServer: {
	hot: true,
    liveReload: false,
        proxy: 'http://172.20.10.2:3000'
    },
    css: { extract: false },
    assetsDir: 'static'
}
