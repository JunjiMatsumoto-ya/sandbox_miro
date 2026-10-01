const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 400, height: 400 }, deviceScaleFactor: 1.5 });
  for (const f of fs.readdirSync('.').filter(f => f.endsWith('.svg'))) {
    await p.setContent(`<html><body style="margin:0;background:transparent">${fs.readFileSync(f,'utf8')}</body></html>`);
    await p.screenshot({ path: f.replace('.svg','.png'), omitBackground: true, clip:{x:0,y:0,width:400,height:400} });
  }
  await b.close();
})();
