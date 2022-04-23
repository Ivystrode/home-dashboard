const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,

  devServer: {
    proxy: {
      '^/api': {
        // target: 'http://localhost:5000', // Use this when testing WITHOUT pinas (ie when not at home)
        target: 'http://192.168.1.84:5000', // use this for pinas (when on home network) - if pinas is running it at the time
        changeOrigin: true,
        pathRewrite: { '^/api': '/'},
      }
    }
  },

  pluginOptions: {
    vuetify: {
			// https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
		}
  }
})
