// vite.config.js
import path from 'path'
import { resolve } from 'path'

export default {
    base: '/static/nodejs/',
    server: {
        host: 'localhost',
        port: 3000,
        open: false,
        watch: {
            usePolling: true,
            disableGlobbing: false,
        },
    },
    module: {
        rules: [
            {
                test: /\.glb$/i,
                use: 'file-loader',
            },
        ],
    },
    build: {
        outDir: '../static_nodejs/nodejs',
        assetsDir: '',
        manifest: true,
        emptyOutDir: true,
        target: 'es2022',
        rollupOptions: {
            input: {
                main: resolve(__dirname, 'src/js/main.js'),
                article: resolve(__dirname, 'src/js/article.js'),
                blog: resolve(__dirname, 'src/js/blog.js'),
                functions: resolve(__dirname, 'src/js/functions.js'),
                instruction: resolve(__dirname, 'src/js/instruction.js'),
                integration: resolve(__dirname, 'src/js/integration.js'),
                loyalty: resolve(__dirname, 'src/js/loyalty.js'),
                price: resolve(__dirname, 'src/js/price.js'),
                tgBot: resolve(__dirname, 'src/js/tg-bot.js'),
                types: resolve(__dirname, 'src/js/types.js'),
                articleCss: resolve(__dirname, 'src/style/article.scss'),
                blogCss: resolve(__dirname,'src/style/blog.scss'),
                functionsCss: resolve(__dirname,'src/style/functions.scss'),
                instructionCss: resolve(__dirname,'src/style/instruction.scss'),
                integrationCss: resolve(__dirname,'src/style/integration.scss'),
                loyaltyCss: resolve(__dirname,'src/style/loyalty.scss'),
                priceCss: resolve(__dirname,'src/style/price.scss'),
                tgBotCss: resolve(__dirname,'src/style/tg-bot.scss'),
                typesCss: resolve(__dirname,'src/style/types.scss'),
                style: resolve(__dirname,'src/style/style.scss'),

            },
            output: {
                entryFileNames: `src/[name].[hash].js`,
                chunkFileNames: `src/[name].[hash].js`,
                assetFileNames: `src/[name].[hash].[ext]`
            }
        },
    },
    resolve: {
        alias: {
            '@': path.resolve(__dirname, 'src'),
        },
    },
}
