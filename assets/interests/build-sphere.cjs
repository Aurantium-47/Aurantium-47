// Bake cong-min/TagCloud's real rotation into standalone animated SVGs for GitHub.
// Upstream code and MIT license are preserved in vendor/.
const fs=require('fs'),path=require('path');
const data=JSON.parse(fs.readFileSync(path.join(__dirname,'interests.json'),'utf8'));
function element(){return {nodeType:1,style:{},offsetWidth:0,offsetHeight:0,appendChild(){},addEventListener(){}};}
global.document={createElement:element};
global.window={matchMedia:()=>({matches:false}),requestAnimationFrame:()=>0};
const TagCloud=require('./vendor/tagcloud.js');
const escape=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
// Explicit positions let appended words join without redistributing existing orbits.
const cloud=TagCloud(element(),data.words.filter(w=>!w.position).map(w=>w.text),{radius:200,keep:true,maxSpeed:'normal',initSpeed:'normal'});
let autoIndex=0;
cloud.items=data.words.map(w=>w.position
 ?{el:element(),...w.position,scale:(2*cloud.depth/(2*cloud.depth+w.position.z)).toFixed(3)}
 :cloud.items[autoIndex++]);
// Equal rotations around two axes. Choose a step with an exact 600-step full turn.
const steps=600,samples=60,theta=2*Math.PI/steps;
const stepDegrees=Math.acos(2*Math.cos(theta/2)-1)*180/Math.PI;
cloud.mouseX=cloud.mouseY=stepDegrees*cloud.radius/cloud.maxSpeed;
cloud.active=true;
const frames=[];
function capture(){return cloud.items.map(item=>({x:item.x,y:item.y,z:item.z,scale:Number(item.scale)}));}
for(let i=0;i<=steps;i++){
  if(i%(steps/samples)===0)frames.push(capture());
  cloud._next();
}
const closure=Math.max(...frames[0].map((p,i)=>Math.hypot(p.x-frames.at(-1)[i].x,p.y-frames.at(-1)[i].y,p.z-frames.at(-1)[i].z)));
if(closure>1e-5)throw new Error('Rotation does not close: '+closure);
frames[frames.length-1]=frames[0];
const period=data.sphere.period_seconds;
function make(mobile,zh){
 const w=mobile?440:920,h=mobile?530:520,cx=w/2,cy=(57+h-52)/2;
 const [sx,baseSy]=data.sphere[mobile?'mobile_spread':'desktop_spread'];
 const sy=baseSy*(h-109)/((mobile?610:600)-109);
 const m=(mobile?.69:1)*800/920;
 let css='',body='';
 data.words.forEach((word,i)=>{
  const label=zh?word.zh:word.text;
  let keys='';
  frames.forEach((frame,n)=>{
   const p=frame[i],x=cx+p.x*sx,y=cy+p.y*sy;
   const a=.2+.8*Math.max(0,Math.min(1,(1-p.z/150)/2));
   keys+=`${(n*100/samples).toFixed(3)}%{transform:translate(${x.toFixed(2)}px,${y.toFixed(2)}px) scale(${p.scale});opacity:${a.toFixed(3)}}`;
  });
  css+=`@keyframes word${i}{${keys}}`;
  const p=frames[0][i];
  body+=`<g class="word" style="animation:word${i} ${period}s linear infinite;transform:translate(${(cx+p.x*sx).toFixed(2)}px,${(cy+p.y*sy).toFixed(2)}px) scale(${p.scale})"><text text-anchor="middle" dominant-baseline="middle" font-size="${(word.size*m).toFixed(1)}"${word.italic?' font-style="italic"':''}>${escape(label)}</text></g>`;
 });
 const note=zh?'AI 根据对话整理维护':'AI-curated & maintained';
 const y=h-27,start=mobile?185:205;
 const stripTop=y-25,stripCenter=(stripTop+h)/2;
 const ticker=[0,1080].map(offset=>`<text x="${start+offset}" y="${stripCenter}" dominant-baseline="central" textLength="1040" lengthAdjust="spacing">${escape(data.attitude.tail)}</text>`).join('');
 return `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" role="img" aria-labelledby="title desc"><title id="title">${escape(note)}</title><desc id="desc">${escape(data.words.map(x=>zh?x.zh:x.text).join(' · '))}</desc>
<style>text{font-family:Georgia,'Noto Serif SC','Microsoft YaHei',serif;fill:#263b2b}${css}.ticker{animation:flow 66s linear infinite}@keyframes flow{to{transform:translateX(-1080px)}}@media(prefers-reduced-motion:reduce){.word,.ticker{animation:none!important;opacity:1}}</style>
<rect width="${w}" height="${h}" rx="4" fill="#f2f1eb"/><text x="28" y="38" font-size="${mobile?18:20}" font-weight="400" opacity="1">${escape(note)}</text><path d="M28 57H${w-28}" stroke="#cdd2c6"/>
${body}<path d="M28 ${stripTop}H${w-28}" stroke="#cdd2c6"/><text x="28" y="${stripCenter}" dominant-baseline="central" font-size="${mobile?16:18}" font-weight="400" opacity="1">${escape(data.attitude.lead)}</text><defs><clipPath id="strip"><rect x="${start}" y="${stripCenter-12.5}" width="${w-start-28}" height="25"/></clipPath></defs><g clip-path="url(#strip)" style="font:12px 'Microsoft YaHei',sans-serif;fill:#7d8976"><g class="ticker">${ticker}</g></g></svg>`;
}
for(const mobile of [false,true])for(const zh of [false,true]){
 const name=`words${mobile?'-mobile':''}${zh?'-zh':''}.svg`;
 fs.writeFileSync(path.join(__dirname,name),make(mobile,zh));console.log(name);
}
console.log(JSON.stringify({upstream:'cong-min/TagCloud',samples,closure,period,minimumOpacity:.2}));
