const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath: process.env.NODE_ENV === 'production'? '/frontend/':'/',
  transpileDependencies: true,
  productionSourceMap: false,
  devServer: {
    proxy: 'http://0.0.0.0:8000'
  }
})
