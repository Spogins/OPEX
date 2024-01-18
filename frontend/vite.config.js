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
        target: 'es2015',
        rollupOptions: {
            input: {
                main: resolve(__dirname, 'js/main.js'),



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
