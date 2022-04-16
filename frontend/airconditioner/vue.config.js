const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  productionSourceMap: false,  
  devServer: {
    proxy: 'http://0.0.0.0:8000',  
  }  
})
