var _t=Object.defineProperty;var kt=(e,t,o)=>t in e?_t(e,t,{enumerable:!0,configurable:!0,writable:!0,value:o}):e[t]=o;var Ge=(e,t,o)=>kt(e,typeof t!="symbol"?t+"":t,o);import{g as z,c as St,u as dt,r as f,a as U,j as n,C as Rt,P as Lt,E as Et,L as V,b as xe,d as Nt,e as Tt}from"./vendor-DLitdnVk.js";import{BoxGeometry as BoxGeom,CylinderGeometry as CylGeom,PlaneGeometry as PlaneGeom,SphereGeometry as SphereGeom,C as B,u as Ct,v as Ae,t as De,S as Ot,b as ke,V as W,Q as At,w as Dt,x as It,y as Bt}from"./three-BkTIaXF_.js";(function(){const t=document.createElement("link").relList;if(t&&t.supports&&t.supports("modulepreload"))return;for(const s of document.querySelectorAll('link[rel="modulepreload"]'))r(s);new MutationObserver(s=>{for(const i of s)if(i.type==="childList")for(const c of i.addedNodes)c.tagName==="LINK"&&c.rel==="modulepreload"&&r(c)}).observe(document,{childList:!0,subtree:!0});function o(s){const i={};return s.integrity&&(i.integrity=s.integrity),s.referrerPolicy&&(i.referrerPolicy=s.referrerPolicy),s.crossOrigin==="use-credentials"?i.credentials="include":s.crossOrigin==="anonymous"?i.credentials="omit":i.credentials="same-origin",i}function r(s){if(s.ep)return;s.ep=!0;const i=o(s);fetch(s.href,i)}})();const Y=[{"id":"automacao","name":"Automação 24/7","label":"#10b981","ink":"#ffffff","finish":{"metalness":0.6,"roughness":0.22,"clearcoat":1,"clearcoatRoughness":0.04},"world":"#00e5ff","accent":"#34d399","notes":"Frya IA · WhatsApp 24/7 · Sub-3s","line":"Atendimento inteligente que nunca dorme.","description":"Agente de IA Frya atendendo, qualificando leads e agendando reuniões no WhatsApp em menos de 3 segundos, 24 horas por dia."},{"id":"google-maps","name":"Google Maps Local","label":"#1e40af","ink":"#ffffff","finish":{"metalness":0.7,"roughness":0.2,"clearcoat":1,"clearcoatRoughness":0.04},"world":"#3b82f6","accent":"#60a5fa","notes":"Top 1 Google · Avaliações 5.0★ · SEO Local","line":"Domine a primeira posição da sua cidade.","description":"Posicione sua empresa no topo absoluto das buscas locais do Google, atraindo clientes qualificados prontos para fechar contrato."},{"id":"instagram-pro","name":"Instagram PRO","label":"#c026d3","ink":"#ffffff","finish":{"metalness":0.85,"roughness":0.15,"clearcoat":1,"clearcoatRoughness":0.04},"world":"#ec4899","accent":"#f472b6","notes":"Bio Estratégica · Carrosséis · Destaques 4K","line":"Perfil magnético que converte seguidores em vendas.","description":"Posicionamento visual e estratégico de alto padrão no Instagram: bio irresistível, carrosséis semanais de autoridade e destaques que vendem."},{"id":"landing-pages","name":"Landing Pages","label":"#0284c7","ink":"#ffffff","finish":{"metalness":0.85,"roughness":0.15,"clearcoat":1,"clearcoatRoughness":0.04},"world":"#06b6d4","accent":"#22d3ee","notes":"Velocidade Sub-s · Mobile First · A/B Tests","line":"Carregamento instantâneo, zero fricção.","description":"Landing pages construídas com tecnologia de ponta, carregamento em menos de 0.8s, copywriting persuasivo e alta taxa de conversão."},{"id":"trafego-pago","name":"Tráfego Pago","label":"#2563eb","ink":"#ffffff","finish":{"metalness":0.6,"roughness":0.22,"clearcoat":1,"clearcoatRoughness":0.04},"world":"#3b82f6","accent":"#93c5fd","notes":"Meta Ads · Google Ads · ROI Comprovado","line":"Escala previsível com leads qualificados.","description":"Gestão profissional de anúncios no Google e Meta, direcionando tráfego qualificado para fechar negócios com o menor custo de aquisição."},{"id":"audiovisual","name":"Audiovisual AI","label":"#dc2626","ink":"#ffffff","finish":{"metalness":0.5,"roughness":0.28,"clearcoat":1,"clearcoatRoughness":0.04},"world":"#ef4444","accent":"#f87171","notes":"HyperFrames · Som Contextual · Sem Intro","line":"Conteúdo cinematográfico que prende a atenção.","description":"Produção de vídeos curtos, Reels e criativos de vendas no padrão DLuz: ritmo acelerado, cortes secos, alternância de planos e retenção máxima."},{"id":"ia-corporativa","name":"IA Corporativa","label":"#7c3aed","ink":"#ffffff","finish":{"metalness":0.65,"roughness":0.22,"clearcoat":1,"clearcoatRoughness":0.04},"world":"#8b5cf6","accent":"#c4b5fd","notes":"Agentes Autônomos · CRMs · Automações","line":"Automatize processos e multiplique a produtividade.","description":"Desenvolvimento de agentes de inteligência artificial personalizados integrados ao ecossistema da sua empresa para multiplicar a capacidade produtiva."},{"id":"reputacao","name":"Reputação 5★","label":"#d97706","ink":"#ffffff","finish":{"metalness":0.85,"roughness":0.2,"clearcoat":1,"clearcoatRoughness":0.06},"world":"#f59e0b","accent":"#fcd34d","notes":"Google Reviews · Prova Social · Filtro Inteligente","line":"Confiança inabalável no piloto automático.","description":"Esteira automatizada que solicita e direciona avaliações 5 estrelas no Google dos seus clientes mais satisfeitos, blindando sua reputação."},{"id":"exclusividade","name":"Exclusividade","label":"#334155","ink":"#ffffff","finish":{"metalness":0.55,"roughness":0.35,"clearcoat":0.9,"clearcoatRoughness":0.1},"world":"#64748b","accent":"#94a3b8","notes":"Blindagem Regional · Sem Conflito · Foco Total","line":"Atendemos apenas uma empresa por nicho na sua região.","description":"Garantia contratual de exclusividade: não atendemos seus concorrentes na mesma área de atuação enquanto durar nossa parceria."},{"id":"consultoria-vip","name":"Consultoria VIP","label":"#0f172a","ink":"#f1e6d2","finish":{"metalness":0.4,"roughness":0.45,"clearcoat":0.8,"clearcoatRoughness":0.2},"world":"#e2e8f0","accent":"#cbd5e1","notes":"Duilio Luz · Conselho Estratégico · Escala","line":"Acompanhamento direto e visão executiva de escala.","description":"Sessões estratégicas diretas com a diretoria da DLuz Digital para desenhar o plano de crescimento, otimizar funis e acelerar os lucros."}],Ne={fov:26,z:19},Ft=0,M=10,ce=e=>e,Yt={p:[0,.42,1.7],r:[.02,0,-.018],s:.88},Ht={p:[0,.5,1.2],r:[.02,0,-.018],s:.74};function ft(e){return e<.85?{rx:4.4*(e/.5),rz:6,step:.4,tilt:.06,y:.35,s:.64,hero:Ht}:{rx:11*Math.max(e/1.78,.72),rz:10,step:.26,tilt:.075,y:.1,s:.74,hero:Yt}}const qt=e=>ft(e).hero.p,Ut=Array.from({length:M},(e,t)=>({roll:(t*37%7-3)*.035,yaw:(t*53%5-2)*.06,pitch:(t*29%5-2)*.03})),$t=(e,t,o)=>{const r=Math.min(1,Math.max(0,(o-e)/(t-e)));return r*r*(3-2*r)};function Xt(e,t,o,r){const s=ft(t),i=s.hero,c=e*s.step,u=Math.exp(-e*e*2.6),l=Ut[o],p=s.rx*Math.sin(c),m=s.rz*(Math.cos(c)-1),g=s.y+p*s.tilt;r.p[0]=p,r.p[1]=g+(i.p[1]-g)*u,r.p[2]=m+i.p[2]*u,r.r[0]=i.r[0]*u+(1-u)*(.05+l.pitch),r.r[1]=c*.9+(1-u)*l.yaw,r.r[2]=i.r[2]*u+(1-u)*(-.08*Math.sin(c)+l.roll);const a=$t(M/2,M/2-.7,Math.abs(e));return r.s=(s.s+(i.s-s.s)*u)*a,r.h=u,r}const Qe={"-5":[-.04,-.12],"-4":[-.08,-.24],"-3":[-.05,-.16],"-2":[-.1,-.32],"-1":[-.06,-.24],0:[-.1,.3],1:[-.07,.12],2:[-.1,.18],3:[-.06,.3],4:[-.05,.36],5:[-.04,.12]};function Vt(e,t){const o=Math.max(-5,Math.min(5,e)),r=Math.floor(o),s=Math.min(5,r+1);let i=o-r;i=i*i*(3-2*i);const c=Qe[r],u=Qe[s];return t.p=c[0]+(u[0]-c[0])*i,t.r=c[1]+(u[1]-c[1])*i,t}const h={from:new B("#000000"),to:new B("#000000"),current:new B("#000000"),studio:new B("#9097a3"),rim:new B("#000000"),progress:1,kick:0,lit:-1,drive:{x:0,y:0,vx:0,vy:0}},I={x:0,y:0};typeof window<"u"&&(window.addEventListener("pointermove",e=>{e.pointerType!=="touch"&&(I.x=e.clientX/window.innerWidth*2-1,I.y=-(e.clientY/window.innerHeight*2-1))}),document.addEventListener("pointerleave",()=>{I.x=0,I.y=0}),window.addEventListener("blur",()=>{I.x=0,I.y=0}));const Je=16;function Zt(e){const t=h.drive;t.vx+=(I.x-t.x)*Je*e,t.vy+=(I.y-t.y)*Je*e;const o=Math.exp(-6.5*e);t.vx*=o,t.vy*=o,t.x+=t.vx*e,t.y+=t.vy*e}const pt={r:255,g:255,b:255},Wt="#e8e8ee";function Kt(){const{r:e,g:t,b:o}=pt;document.documentElement.style.setProperty("--accent-rgb",`${e|0} ${t|0} ${o|0}`)}function Te(e,{delay:t=.12}={}){h.from.copy(h.current),h.to.set(e.world),z.killTweensOf(h),h.progress=0,z.to(h,{progress:1,duration:2.6,delay:t,ease:"power2.out"}),z.fromTo(h,{kick:0},{kick:1,duration:1.8,ease:"power1.out",delay:t});const o=parseInt(Wt.slice(1),16),r=o>>16&255,s=o>>8&255,i=o&255;z.to(pt,{r,g:s,b:i,duration:1.4,delay:t+.25,ease:"power2.inOut",overwrite:!0,onUpdate:Kt})}function Gt(){const e=h.progress,t=e*e*(3-2*e);h.current.lerpColors(h.from,h.to,Math.min(1,t*1.15));const o=h.studio,r=.2126*o.r+.7152*o.g+.0722*o.b;h.rim.copy(o).multiplyScalar(.3/(r+.12))}const mt=260,Qt=2*Math.sqrt(mt),gt=34,Jt=2*Math.sqrt(gt)*.86,en=.34,et=22,ht=150,Ce=6,d={pos:0,vel:0,target:0,held:!1,locked:!1,grab:0,grabPx:0,travel:0,handV:0,lastPx:0,lastT:0,wheelT:0,itemsPerPx:1/300,itemsPerWheelPx:1/320};function se(e,t=d.pos){const o=M;let r=(e-t)%o;return r<-o/2&&(r+=o),r>=o/2&&(r-=o),r}const xt=(e=d.pos)=>(Math.round(e)%M+M)%M;function tn(){return!d.held&&performance.now()-d.wheelT>ht&&Math.abs(d.pos-d.target)<.012&&Math.abs(d.vel)<.06}function tt(e){d.locked||(d.target=Math.round(d.target)+e)}function nt(){d.target=Math.round(d.pos)}const ve=new Set,nn=e=>(ve.add(e),()=>ve.delete(e)),Z={el:null,hover:!1};function ie(){if(Z.el){if(d.locked){Z.el.style.cursor="";return}Z.el.style.cursor=d.held&&d.travel>Ce?"grabbing":Z.hover?"pointer":"grab"}}const ot=()=>ie();function Se(e){Z.hover=e,ie()}function on(e,t){Z.el=e,d.itemsPerPx=1/(t*.34),ie();const o=c=>{c.button!==0||d.locked||(d.held=!0,d.travel=0,d.grab=d.pos,d.grabPx=d.lastPx=c.clientX,d.lastT=performance.now(),d.handV=0,ve.forEach(u=>u(!0)))},r=c=>{if(!d.held)return;const u=performance.now(),l=Math.max((u-d.lastT)/1e3,1/240),p=-(c.clientX-d.lastPx)*d.itemsPerPx/l;d.handV=d.handV*.65+p*.35,d.lastPx=c.clientX,d.lastT=u,d.travel=Math.max(d.travel,Math.abs(c.clientX-d.grabPx)),d.target=d.grab-(c.clientX-d.grabPx)*d.itemsPerPx,ie()},s=()=>{if(!d.held)return;d.held=!1;const u=performance.now()-d.lastT>90?0:Math.max(-et,Math.min(et,d.handV));d.vel=u,d.target=Math.round(d.pos+u*en),ie(),ve.forEach(l=>l(!1))},i=c=>{if(c.preventDefault(),d.locked)return;const u=c.deltaMode===1?16:c.deltaMode===2?window.innerHeight:1,l=(Math.abs(c.deltaX)>Math.abs(c.deltaY)?c.deltaX:c.deltaY)*u;d.target+=l*d.itemsPerWheelPx,d.target=d.pos+Math.max(-4,Math.min(4,d.target-d.pos)),d.wheelT=performance.now()};return e.addEventListener("pointerdown",o),e.addEventListener("wheel",i,{passive:!1}),window.addEventListener("pointermove",r),window.addEventListener("pointerup",s),window.addEventListener("pointercancel",s),window.addEventListener("blur",s),()=>{e.removeEventListener("pointerdown",o),e.removeEventListener("wheel",i),window.removeEventListener("pointermove",r),window.removeEventListener("pointerup",s),window.removeEventListener("pointercancel",s),window.removeEventListener("blur",s)}}function rn(e){if(!d.held&&performance.now()-d.wheelT>ht){const i=Math.round(d.target);i!==d.target&&(d.target=i)}const t=d.held?mt:gt,o=d.held?Qt:Jt,r=4,s=e/r;for(let i=0;i<r;i++)d.vel+=((d.target-d.pos)*t-d.vel*o)*s,d.pos+=d.vel*s}const q=[{"id":"resposta","icon":"bolt","label":"Sub-3s","crossedOut":"Espera e Perda de Vendas","title":["Resposta","Instantânea"],"description":"Atendimento inteligente que responde leads em segundos no WhatsApp, convertendo contatos antes que procurem concorrentes.","rotationY":-10,"focusY":0,"tilt":5},{"id":"exclusividade","icon":"leaf","label":"100%","crossedOut":"Concorrência Desleal","title":["Exclusividade","Territorial"],"description":"Atendemos exclusivamente uma única empresa por segmento na sua cidade ou região para blindar o seu crescimento.","rotationY":170,"focusY":0,"tilt":5},{"id":"design","icon":"cube","label":"Ultra-Fast","crossedOut":"Sites Lentos e Genéricos","title":["Design","Executivo"],"description":"Interfaces modernas, landing pages com carregamento abaixo de 1 segundo e presença de marca com padrão internacional.","rotationY":-8,"focusY":0.05,"tilt":4},{"id":"ia","icon":"sparkle","label":"IA Real","crossedOut":"Workflows Manuais","title":["Automação","& Retorno"],"description":"Agentes autônomos treinados para executar processos, qualificar clientes e maximizar o retorno sobre o seu investimento.","rotationY":12,"focusY":-0.05,"tilt":6}],he={rotationY:-10,focusY:0,tilt:6},ye=e=>e*Math.PI/180,b={k:0,item:-1,yaw:ye(he.rotationY),focusY:he.focusY,tilt:ye(he.tilt),zoom:0,spot:0},vt=e=>{const t=e<0?he:q[e];return{yaw:ye(t.rotationY),focusY:t.focusY,tilt:ye(t.tilt),zoom:e<0?0:1,spot:e<0?0:1}};function Ie(e,{duration:t=1}={}){z.to(b,{...vt(e),duration:t,ease:"power3.inOut",overwrite:"auto"})}function sn(e){b.k<.001&&Object.assign(b,vt(-1)),b.item=e,Ie(-1,{duration:1.2}),z.to(b,{k:1,duration:1.45,ease:"power3.inOut",overwrite:"auto"})}function an(e){Ie(-1,{duration:1}),z.to(b,{k:0,duration:1.3,ease:"power3.inOut",overwrite:"auto",onComplete:()=>{b.item=-1,e?.()}})}const cn={x:1.05,y:.05,z:6,s:1.34,rx:.06},ln={x:.9,y:.1,z:7.2,s:1.6,rx:.02},un={x:.15,y:.75,z:4.2,s:.9,rx:.05},dn={x:.1,y:1,z:5.4,s:1.15,rx:.02},oe=(e,t,o)=>e+(t-e)*o;function Be(e,t){const o=e<.85,r=o?un:cn,s=o?dn:ln,i=b.zoom,c=oe(r.s,s.s,i);return t.s=c,t.p[0]=oe(r.x,s.x,i),t.p[1]=oe(r.y,s.y-b.focusY*c,i),t.p[2]=oe(r.z,s.z,i),t.rx=oe(r.rx,s.rx,i),t.rz=b.tilt,t.yaw=b.yaw,t}const Re=(e,t)=>{const o=Math.abs(e-t)%M;return Math.min(o,M-o)};function yt(e){const t=new Array(M);return e.forEach((o,r)=>t[o]=ce(r)),t}function rt(e){const t=yt(e);let o=0;for(let r=0;r<M;r++)t[r]===t[(r+1)%M]&&o++;return o}function fn(e,t){let o=e.slice();for(let r=0;r<M&&rt(o)>0;r++){const s=yt(o);let i=0;for(;s[i]!==s[(i+1)%M];)i++;const c=i,u=(i+1)%M,l=c===t?u:u===t||Re(c,t)>=Re(u,t)?c:u,p=o.indexOf(l);let m=null;for(let g=0;g<M;g++){if(g===t||g===l)continue;const a=o.slice(),w=a.indexOf(g);a[p]=g,a[w]=l;const _=[rt(a),-Re(g,t)];(!m||_[0]<m.score[0]||_[0]===m.score[0]&&_[1]<m.score[1])&&(m={trial:a,score:_})}o=m.trial}return o}const pn=Array.from({length:M},(e,t)=>t),mn=(e,t)=>e.indexOf(t),P=St((e,t)=>({active:0,slotOf:pn,hovered:null,ready:!1,mode:"hero",benefit:-1,setReady:()=>{if(t().ready)return;e({ready:!0});const o=t().active;h.lit=o,Te(Y[o],{delay:.9})},setHovered:o=>e({hovered:o}),setActive:o=>{o!==t().active&&e({active:o})},swapItem:o=>{nt();const r=t().slotOf,s=xt(d.target);if(r[o]===s)return!1;const i=mn(r,s);let c=r.slice();c[i]=r[o],c[o]=s,c=fn(c,s);const u=ce(o);return e({slotOf:c,active:u}),h.lit=u,Te(Y[u]),!0},openDetail:o=>{nt(),d.locked=!0,ot(),e({mode:"detail",benefit:-1,hovered:null}),sn(o)},closeDetail:()=>{t().mode==="detail"&&(e({mode:"hero",benefit:-1}),an(()=>{t().mode==="hero"&&(d.locked=!1,ot())}))},setBenefit:o=>{if(t().mode!=="detail")return;const r=q.length,s=o<0?-1:o%r;s!==t().benefit&&(e({benefit:s}),Ie(s))},goTo:o=>{const r=t().slotOf,s=Math.round(d.target);let i=null;r.forEach((c,u)=>{if(ce(u)!==o)return;const l=Math.round(se(c,s));(i===null||Math.abs(l)<Math.abs(i))&&(i=l)}),i&&tt(i)},step:o=>tt(o)})),wt=new URL("../models/blazing-can-hd.glb",import.meta.url).href;function st(e){const t=e.clone();return t.rotateX(-Math.PI/2),t.translate(0,-.13,0),t.computeBoundingSphere(),t}function me(e,t,o){const r=e.attributes.position,s=e.index.array,i=[],c=l=>{const p=r.getY(l);return p>=t&&p<=o};for(let l=0;l<s.length;l+=3){const p=s[l],m=s[l+1],g=s[l+2];c(p)&&c(m)&&c(g)&&i.push(p,m,g)}const u=new Ct;for(const l in e.attributes)u.setAttribute(l,e.attributes[l]);return u.setIndex(i),u.computeBoundingSphere(),u}
const _geomPhoneBody = new BoxGeom(1.12, 2.42, 0.08);
const _geomPhoneScreen = new PlaneGeom(1.06, 2.34);
const _geomPhoneBack = new PlaneGeom(1.06, 2.34);
const _geomPhoneCam = new BoxGeom(0.44, 0.44, 0.035);
const _geomPhoneLens = new CylGeom(0.085, 0.085, 0.025, 24);
const _geomPhoneFlash = new CylGeom(0.04, 0.04, 0.02, 16);
const _geomPhoneLabel = new PlaneGeom(1.34, 0.38);

const _matBlackGlass = new Ae({ color: "#06070a", roughness: 0.06, metalness: 0.95 });
const _matFlash = new Ae({ color: "#fffaed", roughness: 0.3, emissive: "#fffaed", emissiveIntensity: 0.8 });
const _matTitaniumChassis = new Ae({ color: "#181a20", metalness: 0.95, roughness: 0.22, clearcoat: 0.8 });

window.__dluzScreens = [];
window.__dluzLabels = [];
window.__dluzPhoneBack = null;

function gn(){
  const {nodes: e, materials: t} = dt(wt);
  return f.useMemo(()=>{
    t.Body.map.anisotropy = 8;
    t.Body.map.needsUpdate = !0;
    
    if (!window.__dluzTexturesLoaded) {
      window.__dluzTexturesLoaded = !0;
      
      // Load all 10 phone screen textures
      for (let idx = 0; idx < 10; idx++) {
        const tex = new t.Body.map.constructor();
        if (t.Body.map.source) {
          tex.source = new t.Body.map.source.constructor();
        }
        tex.anisotropy = 8;
        window.__dluzScreens[idx] = tex;
        
        const img = new Image();
        img.crossOrigin = "anonymous";
        img.src = new URL("./assets/screens/screen_" + idx + ".webp", document.baseURI).href;
        img.onload = () => {
          tex.image = img;
          if (tex.source) {
            tex.source.data = img;
            tex.source.needsUpdate = true;
          }
          tex.needsUpdate = true;
        };
      }
      
      // Load all 10 phone label badge textures
      for (let idx = 0; idx < 10; idx++) {
        const lTex = new t.Body.map.constructor();
        if (t.Body.map.source) {
          lTex.source = new t.Body.map.source.constructor();
        }
        lTex.anisotropy = 8;
        window.__dluzLabels[idx] = lTex;
        
        const lImg = new Image();
        lImg.crossOrigin = "anonymous";
        lImg.src = new URL("./assets/screens/label_" + idx + ".webp", document.baseURI).href;
        lImg.onload = () => {
          lTex.image = lImg;
          if (lTex.source) {
            lTex.source.data = lImg;
            lTex.source.needsUpdate = true;
          }
          lTex.needsUpdate = true;
        };
      }
      
      // Load phone backplate
      const bTex = new t.Body.map.constructor();
      if (t.Body.map.source) {
        bTex.source = new t.Body.map.source.constructor();
      }
      bTex.anisotropy = 8;
      window.__dluzPhoneBack = bTex;
      
      const backImg = new Image();
      backImg.crossOrigin = "anonymous";
      backImg.src = new URL("./assets/screens/phone_back.webp", document.baseURI).href;
      backImg.onload = () => {
        bTex.image = backImg;
        if (bTex.source) {
          bTex.source.data = backImg;
          bTex.source.needsUpdate = true;
        }
        bTex.needsUpdate = true;
      };
    }
    
    const o = st(e.LowRes_Can_Body_0.geometry);
    const r = st(e.LowRes_Can_Alluminium_0.geometry);
    return {
      body: o,
      alu: r,
      lid: { body: me(o, .9, 3), alu: me(r, .9, 3) },
      base: { body: me(o, -3, -.9), alu: me(r, -3, -.9) },
      source: { body: t.Body, alu: t.Alluminium }
    };
  }, [e, t]);
}
dt.preload(wt);const bt=`
vec4 permute(vec4 x){return mod(((x*34.0)+1.0)*x, 289.0);}
vec4 taylorInvSqrt(vec4 r){return 1.79284291400159 - 0.85373472095314 * r;}
vec4 fade(vec4 t) {return t*t*t*(t*(t*6.0-15.0)+10.0);}

float cnoise(vec4 P){
  ;
  vec4 Pi0 = floor(P);
  vec4 Pi1 = Pi0 + 1.0;
  Pi0 = mod(Pi0, 289.0);
  Pi1 = mod(Pi1, 289.0);
  vec4 Pf0 = fract(P);
  vec4 Pf1 = Pf0 - 1.0;
  vec4 ix = vec4(Pi0.x, Pi1.x, Pi0.x, Pi1.x);
  vec4 iy = vec4(Pi0.yy, Pi1.yy);
  vec4 iz0 = vec4(Pi0.zzzz);
  vec4 iz1 = vec4(Pi1.zzzz);
  vec4 iw0 = vec4(Pi0.wwww);
  vec4 iw1 = vec4(Pi1.wwww);

  vec4 ixy = permute(permute(ix) + iy);
  vec4 ixy0 = permute(ixy + iz0);
  vec4 ixy1 = permute(ixy + iz1);
  vec4 ixy00 = permute(ixy0 + iw0);
  vec4 ixy01 = permute(ixy0 + iw1);
  vec4 ixy10 = permute(ixy1 + iw0);
  vec4 ixy11 = permute(ixy1 + iw1);

  vec4 gx00 = ixy00 / 7.0;
  vec4 gy00 = floor(gx00) / 7.0;
  vec4 gz00 = floor(gy00) / 6.0;
  gx00 = fract(gx00) - 0.5;
  gy00 = fract(gy00) - 0.5;
  gz00 = fract(gz00) - 0.5;
  vec4 gw00 = vec4(0.75) - abs(gx00) - abs(gy00) - abs(gz00);
  vec4 sw00 = step(gw00, vec4(0.0));
  gx00 -= sw00 * (step(0.0, gx00) - 0.5);
  gy00 -= sw00 * (step(0.0, gy00) - 0.5);

  vec4 gx01 = ixy01 / 7.0;
  vec4 gy01 = floor(gx01) / 7.0;
  vec4 gz01 = floor(gy01) / 6.0;
  gx01 = fract(gx01) - 0.5;
  gy01 = fract(gy01) - 0.5;
  gz01 = fract(gz01) - 0.5;
  vec4 gw01 = vec4(0.75) - abs(gx01) - abs(gy01) - abs(gz01);
  vec4 sw01 = step(gw01, vec4(0.0));
  gx01 -= sw01 * (step(0.0, gx01) - 0.5);
  gy01 -= sw01 * (step(0.0, gy01) - 0.5);

  vec4 gx10 = ixy10 / 7.0;
  vec4 gy10 = floor(gx10) / 7.0;
  vec4 gz10 = floor(gy10) / 6.0;
  gx10 = fract(gx10) - 0.5;
  gy10 = fract(gy10) - 0.5;
  gz10 = fract(gz10) - 0.5;
  vec4 gw10 = vec4(0.75) - abs(gx10) - abs(gy10) - abs(gz10);
  vec4 sw10 = step(gw10, vec4(0.0));
  gx10 -= sw10 * (step(0.0, gx10) - 0.5);
  gy10 -= sw10 * (step(0.0, gy10) - 0.5);

  vec4 gx11 = ixy11 / 7.0;
  vec4 gy11 = floor(gx11) / 7.0;
  vec4 gz11 = floor(gy11) / 6.0;
  gx11 = fract(gx11) - 0.5;
  gy11 = fract(gy11) - 0.5;
  gz11 = fract(gz11) - 0.5;
  vec4 gw11 = vec4(0.75) - abs(gx11) - abs(gy11) - abs(gz11);
  vec4 sw11 = step(gw11, vec4(0.0));
  gx11 -= sw11 * (step(0.0, gx11) - 0.5);
  gy11 -= sw11 * (step(0.0, gy11) - 0.5);

  vec4 g0000 = vec4(gx00.x,gy00.x,gz00.x,gw00.x);
  vec4 g1000 = vec4(gx00.y,gy00.y,gz00.y,gw00.y);
  vec4 g0100 = vec4(gx00.z,gy00.z,gz00.z,gw00.z);
  vec4 g1100 = vec4(gx00.w,gy00.w,gz00.w,gw00.w);
  vec4 g0010 = vec4(gx10.x,gy10.x,gz10.x,gw10.x);
  vec4 g1010 = vec4(gx10.y,gy10.y,gz10.y,gw10.y);
  vec4 g0110 = vec4(gx10.z,gy10.z,gz10.z,gw10.z);
  vec4 g1110 = vec4(gx10.w,gy10.w,gz10.w,gw10.w);
  vec4 g0001 = vec4(gx01.x,gy01.x,gz01.x,gw01.x);
  vec4 g1001 = vec4(gx01.y,gy01.y,gz01.y,gw01.y);
  vec4 g0101 = vec4(gx01.z,gy01.z,gz01.z,gw01.z);
  vec4 g1101 = vec4(gx01.w,gy01.w,gz01.w,gw01.w);
  vec4 g0011 = vec4(gx11.x,gy11.x,gz11.x,gw11.x);
  vec4 g1011 = vec4(gx11.y,gy11.y,gz11.y,gw11.y);
  vec4 g0111 = vec4(gx11.z,gy11.z,gz11.z,gw11.z);
  vec4 g1111 = vec4(gx11.w,gy11.w,gz11.w,gw11.w);

  vec4 norm00 = taylorInvSqrt(vec4(dot(g0000, g0000), dot(g0100, g0100), dot(g1000, g1000), dot(g1100, g1100)));
  g0000 *= norm00.x;
  g0100 *= norm00.y;
  g1000 *= norm00.z;
  g1100 *= norm00.w;

  vec4 norm01 = taylorInvSqrt(vec4(dot(g0001, g0001), dot(g0101, g0101), dot(g1001, g1001), dot(g1101, g1101)));
  g0001 *= norm01.x;
  g0101 *= norm01.y;
  g1001 *= norm01.z;
  g1101 *= norm01.w;

  vec4 norm10 = taylorInvSqrt(vec4(dot(g0010, g0010), dot(g0110, g0110), dot(g1010, g1010), dot(g1110, g1110)));
  g0010 *= norm10.x;
  g0110 *= norm10.y;
  g1010 *= norm10.z;
  g1110 *= norm10.w;

  vec4 norm11 = taylorInvSqrt(vec4(dot(g0011, g0011), dot(g0111, g0111), dot(g1011, g1011), dot(g1111, g1111)));
  g0011 *= norm11.x;
  g0111 *= norm11.y;
  g1011 *= norm11.z;
  g1111 *= norm11.w;

  float n0000 = dot(g0000, Pf0);
  float n1000 = dot(g1000, vec4(Pf1.x, Pf0.yzw));
  float n0100 = dot(g0100, vec4(Pf0.x, Pf1.y, Pf0.zw));
  float n1100 = dot(g1100, vec4(Pf1.xy, Pf0.zw));
  float n0010 = dot(g0010, vec4(Pf0.xy, Pf1.z, Pf0.w));
  float n1010 = dot(g1010, vec4(Pf1.x, Pf0.y, Pf1.z, Pf0.w));
  float n0110 = dot(g0110, vec4(Pf0.x, Pf1.yz, Pf0.w));
  float n1110 = dot(g1110, vec4(Pf1.xyz, Pf0.w));
  float n0001 = dot(g0001, vec4(Pf0.xyz, Pf1.w));
  float n1001 = dot(g1001, vec4(Pf1.x, Pf0.yz, Pf1.w));
  float n0101 = dot(g0101, vec4(Pf0.x, Pf1.y, Pf0.z, Pf1.w));
  float n1101 = dot(g1101, vec4(Pf1.xy, Pf0.z, Pf1.w));
  float n0011 = dot(g0011, vec4(Pf0.xy, Pf1.zw));
  float n1011 = dot(g1011, vec4(Pf1.x, Pf0.y, Pf1.zw));
  float n0111 = dot(g0111, vec4(Pf0.x, Pf1.yzw));
  float n1111 = dot(g1111, Pf1);

  vec4 fade_xyzw = fade(Pf0);
  vec4 n_0w = mix(vec4(n0000, n1000, n0100, n1100), vec4(n0001, n1001, n0101, n1101), fade_xyzw.w);
  vec4 n_1w = mix(vec4(n0010, n1010, n0110, n1110), vec4(n0011, n1011, n0111, n1111), fade_xyzw.w);
  vec4 n_zw = mix(n_0w, n_1w, fade_xyzw.z);
  vec2 n_yzw = mix(n_zw.xy, n_zw.zw, fade_xyzw.y);
  float n_xyzw = mix(n_yzw.x, n_yzw.y, fade_xyzw.x);
  return 2.2 * n_xyzw;
}
`,jt={uTime:{value:0},uRimColor:{value:h.rim}},hn=`
  float rimFres = pow(1.0 - saturate(dot(normal, normalize(vViewPosition))), 3.0);
  outgoingLight += uRimColor * rimFres * uRim;
  outgoingLight *= uLevel;

  outgoingLight = mix(outgoingLight, vec3(dot(outgoingLight, vec3(0.2126, 0.7152, 0.0722))), uDesat);
  #include <opaque_fragment>
`;function Fe(e,t){t.uLevel||(t.uLevel={value:1}),t.uDesat||(t.uDesat={value:0}),Object.assign(e.uniforms,jt,t),e.fragmentShader=e.fragmentShader.replace("#include <common>",`#include <common>
       uniform vec3 uRimColor;
       uniform float uRim;
       uniform float uLevel;
       uniform float uDesat;
       uniform float uTime;`).replace("#include <opaque_fragment>",hn)}function xn(e,t){const o={uBase:{value:new B(t.label)},uInk:{value:new B(t.ink)},uRim:{value:.6},uLevel:{value:1},uDesat:{value:0},uSweep:{value:0},uSweepColor:{value:new B(t.world)}},r=new Ae({map:e.map,normalMap:e.normalMap,normalScale:e.normalScale.clone(),metalness:.55,roughness:.26,clearcoat:1,clearcoatRoughness:.05,side:De,...t.finish});return r.onBeforeCompile=s=>{Fe(s,o),s.fragmentShader=s.fragmentShader.replace("#include <common>",`#include <common>
         uniform vec3 uBase;
         uniform vec3 uInk;
         uniform float uSweep;
         uniform vec3 uSweepColor;
         ${bt}`).replace("#include <map_fragment>",`#include <map_fragment>
         float inkMask = smoothstep(0.02, 0.36, dot(diffuseColor.rgb, vec3(0.2126, 0.7152, 0.0722)));
         diffuseColor.rgb = mix(uBase, uInk, inkMask);`).replace("#include <metalnessmap_fragment>",`#include <metalnessmap_fragment>

         metalnessFactor *= mix(1.0, 0.25, inkMask);
         roughnessFactor = mix(roughnessFactor, 0.42, inkMask);`).replace("#include <opaque_fragment>",`if (uSweep > 0.0 && uSweep < 1.0) {

           float sn = 0.5 * (cnoise(vec4(vMapUv.x * 22.0 + uTime * 0.2, vMapUv.y * 22.0, uTime * 0.25, 0.0)) + 1.0);
           float y = (1.0 - vMapUv.y) + sn * 0.07;
           float head = mix(-0.2, 1.2, uSweep);
           float band = smoothstep(head - 0.22, head, y) * (1.0 - smoothstep(head, head + 0.015, y));
           outgoingLight += uSweepColor * band * 2.2 + pow(band, 8.0) * 1.2;
         }
         #include <opaque_fragment>`)},r.customProgramCacheKey=()=>"blazing-label",r.userData.uniforms=o,r}function vn(e){const t={uRim:{value:.45},uLevel:{value:1},uDesat:{value:0}},o=new Ae({color:"#cfd4db",normalMap:e.normalMap,normalScale:e.normalScale.clone(),metalness:1,roughness:.2,side:De});return o.onBeforeCompile=r=>Fe(r,t),o.customProgramCacheKey=()=>"blazing-alu",o.userData.uniforms=t,o}function at(e,{color:t="#16171b",rim:o=.9,roughness:r=.3,envMapIntensity:s=1}={}){const i={uRim:{value:o}},c=new Ae({color:t,normalMap:e.normalMap,normalScale:e.normalScale.clone(),metalness:1,roughness:r,envMapIntensity:s,side:De});return c.onBeforeCompile=u=>Fe(u,i),c.customProgramCacheKey=()=>"blazing-framer",c.userData.uniforms=i,c}const yn=`
  varying vec2 vUv;
  void main() {
    vUv = uv;

    gl_Position = vec4(position.xy, 0.9999, 1.0);
  }
`,wn=`
  uniform float uTime;
  uniform float uProgress;
  uniform float uAspect;
  uniform vec2 uOrigin;
  uniform vec2 uParallax;
  uniform vec3 uColorB;
  uniform vec3 uStudio;
  uniform vec2 uResolution;

  varying vec2 vUv;

  ${bt}

  float hash(vec2 p) {
    return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453);
  }

  vec3 atmosphere(vec3 c, vec2 p, float d) {

    c *= 0.42 / (dot(c, vec3(0.2126, 0.7152, 0.0722)) + 0.2);
    vec3 col = vec3(0.0025, 0.0025, 0.0035);
    float halo = exp(-d * d * 9.0);
    float wide = exp(-d * d * 2.2);
    float column = exp(-pow(p.x * 3.6, 2.0)) * smoothstep(-0.5, 0.45, p.y);
    float floorPool = exp(-pow((p.y + 0.5) * 5.0, 2.0)) * exp(-pow(p.x * 1.4, 2.0));

    col += c * (halo * 0.19 + wide * 0.022 + column * 0.034 + floorPool * 0.06);
    return col;
  }

  void main() {
    float t = uTime;
    vec2 p = (vUv - uOrigin) * vec2(uAspect, 1.0) + uParallax;
    float d = length(p);

    vec2 far = max(uOrigin, 1.0 - uOrigin) * vec2(uAspect, 1.0);
    float R = length(far) * 1.12 + 0.12;

    float prog = uProgress;
    float wave = step(prog, 0.999);
    float dw = d;
    if (wave > 0.5) {

      dw += cnoise(vec4(p * 2.3, t * 0.35, 0.0)) * 0.075
          + cnoise(vec4(p * 8.5, t * 0.9, 3.0)) * 0.02;
    }

    float outerP = clamp(1.1 * prog, 0.0, 1.0);
    float innerP = clamp(1.1 * prog - 0.05, 0.0, 1.0);
    float innerCircle = 1.0 - smoothstep((innerP - 0.4) * R, innerP * R, dw);
    float outerCircle = 1.0 - smoothstep((outerP - 0.1) * R, innerP * R, dw);
    float ring = clamp(outerCircle - innerCircle, 0.0, 1.0);
    ring *= 1.0 - smoothstep(0.72, 1.0, prog);

    float density = 1.8 - d;
    float nz = cnoise(vec4(p * 36.0 * density, t * 0.9, 1.0));
    float dots = smoothstep(0.1, 0.15, nz);
    float n = 1.0 - step(0.2, nz * 2.0) * dots;
    float speck = clamp(ring - (n + nz), 0.0, 1.0);

    speck *= mix(0.4, 1.0, smoothstep(innerP * R - 0.32, innerP * R, dw));

    vec3 col = atmosphere(uStudio, p, d);

    col += uColorB * (speck * 2.1 + ring * ring * 0.2);
    col += vec3(1.0) * pow(speck, 2.0) * 0.25;

    float orbitR = 0.43 + 0.015 * sin(t * 0.6);
    float orbit = exp(-pow((d - orbitR) * 7.0, 2.0));
    col += uStudio * smoothstep(0.3, 0.75, nz) * orbit * 0.07;

    vec2 q = (vUv - 0.5) * vec2(uAspect, 1.0);
    col *= mix(0.45, 1.0, smoothstep(1.15, 0.2, length(q)));

    gl_FragColor = vec4(col, 1.0);
    #include <colorspace_fragment>

    float g = hash(vUv * uResolution + fract(t * 7.13) * 91.7);
    gl_FragColor.rgb += (g - 0.5) * 0.028;
  }
`,re=new W,bn=new W,jn={p:[0,0,0],rx:0,rz:0,s:1,yaw:0};function Pn({center:e}){const t=f.useMemo(()=>new Ot({vertexShader:yn,fragmentShader:wn,depthWrite:!1,depthTest:!1,toneMapped:!1,uniforms:{uTime:{value:0},uProgress:{value:1},uAspect:{value:1},uOrigin:{value:new ke(.5,.5)},uParallax:{value:new ke},uColorB:{value:h.to},uStudio:{value:h.studio},uResolution:{value:new ke(1,1)}}}),[]);return U(({clock:o,size:r,camera:s},i)=>{Gt(),Zt(Math.min(i,1/30));const c=o.elapsedTime,u=t.uniforms;if(jt.uTime.value=c,u.uTime.value=c,u.uProgress.value=h.progress,u.uAspect.value=r.width/r.height,u.uResolution.value.set(r.width,r.height),re.set(e[0],e[1],e[2]),b.k>0){const l=Be(r.width/r.height,jn);re.lerp(bn.set(l.p[0],l.p[1]+l.s*.4,l.p[2]),b.k)}re.project(s),u.uOrigin.value.set(re.x*.5+.5,re.y*.5+.5),u.uParallax.value.set(h.drive.x*-.025,h.drive.y*-.012)}),n.jsx("mesh",{frustumCulled:!1,renderOrder:-10,raycast:()=>null,material:t,children:n.jsx("planeGeometry",{args:[2,2]})})}const it=Math.PI*2,C=(e,t,o,r)=>e+(t-e)*(1-Math.exp(-o*r)),Le=(e,t,o)=>Math.min(o,Math.max(t,e)),R=(e,t,o)=>e+(t-e)*o,zn=new W(1,0,0),Mn=new W(0,0,1),ct=new At;function _n({item:e,assets:t,aspect:o}){const r=f.useRef(),s=ce(e),i=Y[s],c=P(x=>x.slotOf[e]),u=P(x=>x.swapItem),l=P(x=>x.openDetail),p=P(x=>x.setHovered),m=f.useMemo(()=>xn(t.source.body,i),[t,i]),g=f.useMemo(()=>vn(t.source.alu),[t]);f.useEffect(()=>()=>{m.dispose(),g.dispose()},[m,g]);const a=f.useMemo(()=>({slot:c,t:1,from:null,fromH:0,arc:[0,0,0],spinFrom:0,spinTo:0,dpose:{p:[0,0,0],rx:0,rz:0,s:1,yaw:0},intro:0,hover:0,hoverTarget:0,bank:0,pitch:0,lastX:null,lastZ:0,ring:{p:[0,0,0],r:[0,0,0],s:1,h:0},base:{p:new W,r:[0,0,0],s:1,spin:0,h:0},phase:e*1.618,er:{x:0,y:0,z:0},tilt:{p:0,r:0},tiltTarget:{p:0,r:0},ready:!1}),[]);f.useEffect(()=>{const x=Math.min(4,Math.abs(Math.round(se(a.slot))));z.to(a,{intro:1,duration:2.6,delay:.35+(4-x)*.11,ease:"expo.out"})},[a]),f.useEffect(()=>{if(a.slot===c)return;a.slot=c;const x=Math.abs(se(c,d.target))<.5;a.from={p:a.base.p.toArray(),r:[...a.base.r],s:a.base.s},a.fromH=a.base.h,a.arc=x?[0,.8,3.4]:[0,-.9,-2.8],a.spinFrom=a.base.spin,a.spinTo=a.base.spin+(x?it:-it),z.fromTo(a,{t:0},{t:1,duration:x?1.65:1.8,ease:x?"power3.inOut":"power2.inOut",overwrite:"auto"}),x&&z.fromTo(m.userData.uniforms.uSweep,{value:0},{value:1,delay:.9,duration:1.4,ease:"power2.inOut"})},[c,a,m]),U((x,$)=>{const k=r.current;if(!k)return;const S=Math.min($,1/30),H=x.clock.elapsedTime,Ye=se(a.slot),L=Xt(Ye,o,e,a.ring);k.visible=L.s>.001||a.t<1;const v=a.base,O=a.t;if(O<1&&a.from){const j=a.from,ne=1-O;for(let T=0;T<3;T++){const Mt=(j.p[T]+L.p[T])*.5+a.arc[T]*2;v.p.setComponent(T,ne*ne*j.p[T]+2*ne*O*Mt+O*O*L.p[T]),v.r[T]=j.r[T]+(L.r[T]-j.r[T])*O}v.s=j.s+(L.s-j.s)*O,v.h=a.fromH+(L.h-a.fromH)*O}else v.p.fromArray(L.p),v.r[0]=L.r[0],v.r[1]=L.r[1],v.r[2]=L.r[2],v.s=L.s,v.h=L.h;v.spin=a.spinFrom+(a.spinTo-a.spinFrom)*O,a.lastX===null&&(a.lastX=v.p.x,a.lastZ=v.p.z);const He=(v.p.x-a.lastX)/Math.max(S,1e-4),zt=(v.p.z-a.lastZ)/Math.max(S,1e-4);a.lastX=v.p.x,a.lastZ=v.p.z;const be=Math.abs(He)>150;a.bank=C(a.bank,be?a.bank:Le(-He*.03,-.32,.32),5,S),a.pitch=C(a.pitch,be?a.pitch:Le(zt*.02,-.18,.18),5,S);const E=v.h;d.locked&&(a.hoverTarget=0),a.hover=C(a.hover,a.hoverTarget,7,S);const D=a.hover*(1-E*.6),K=a.phase,je=1-a.intro,{x:qe,y:Ue}=h.drive;let G=v.p.x+qe*(.08+.14*E),Q=v.p.y+Math.sin(H*.72+K)*.1+Math.sin(H*.31+K*2.1)*.045+D*.12+Ue*.05-je*je*9,J=v.p.z+D*.75,le=v.r[0]+Math.sin(H*.45+K)*.03-Ue*.06*E+a.pitch;const $e=Ft+v.r[1]+v.spin;let ue=$e+Math.sin(H*.27+K)*.12*(1-E*.5)+qe*(.06+.22*E)-D*.22-je*2.4,de=v.r[2]+Math.cos(H*.5+K)*.025*(1-E*.5)+a.bank,ee=v.s*(1+D*.05)*(.7+.3*a.intro);const y=b.k,te=e===b.item;if(y>0)if(te){const j=Be(o,a.dpose),ne=Math.sin(H*.6)*.04;G=R(G,j.p[0],y),Q=R(Q,j.p[1]+ne,y),J=R(J,j.p[2],y),le=R(le,j.rx,y),ue=R(ue,$e+j.yaw+Math.sin(H*.33)*.025,y),de=R(de,j.rz,y),ee=R(ee,j.s,y)}else{const j=Math.sign(v.p.x)||1;G+=j*y*y*7,Q-=y*.6,J-=y*5,ee*=1-.35*y}te||(k.visible=k.visible&&y<.985);const Xe=Vt(Ye,a.tiltTarget),Ve=te?1-y:1,Ze=Xe.p*Ve,We=Xe.r*Ve,N=a.er;!a.ready||be?(k.position.set(G,Q,J),N.x=le,N.y=ue,N.z=de,a.tilt.p=Ze,a.tilt.r=We,k.scale.setScalar(ee),a.ready=!0):(k.position.x=C(k.position.x,G,14,S),k.position.y=C(k.position.y,Q,14,S),k.position.z=C(k.position.z,J,14,S),N.x=C(N.x,le,10,S),N.y=C(N.y,ue,10,S),N.z=C(N.z,de,10,S),a.tilt.p=C(a.tilt.p,Ze,6,S),a.tilt.r=C(a.tilt.r,We,6,S),k.scale.setScalar(C(k.scale.x,ee,14,S))),k.rotation.set(N.x,N.y,N.z),k.quaternion.premultiply(ct.setFromAxisAngle(zn,a.tilt.p)),k.quaternion.premultiply(ct.setFromAxisAngle(Mn,a.tilt.r));const Pe=m.userData.uniforms;let X=.3+.82*E+.32*D,fe=.3+.9*E+D*.9,ze=.26+1.24*E+.4*D,Me=.4+.95*E;const Ke=Le(E+D*.7,0,1);let _e=R(.45,1,Ke),pe=.25*(1-Ke);if(te&&y>0&&(_e=R(_e,1,y),pe=R(pe,0,y)),X*=_e,y>0)if(te){const j=b.spot;X=R(X,1.08-.46*j,y),fe=R(fe,1.35-.55*j,y),ze=R(ze,1.55-.95*j,y),Me=R(Me,1.5,y)}else X*=1-.9*y,fe*=1-y;Pe.uLevel.value=X,Pe.uDesat.value=pe,g.userData.uniforms.uDesat.value=pe,Pe.uRim.value=fe,m.envMapIntensity=ze,g.userData.uniforms.uLevel.value=X,g.userData.uniforms.uRim.value=.25+.55*E,g.envMapIntensity=Me});const w=x=>{x.stopPropagation(),!d.locked&&(a.hoverTarget=1,p(s),Se(!0))},_=()=>{a.hoverTarget=0,P.getState().hovered===s&&p(null),Se(!1)},A=x=>{x.stopPropagation(),!d.locked&&(d.travel>Ce||x.delta>Ce||a.t<.98&&Math.abs(se(a.slot))<.5||u(e)||(a.hoverTarget=0,Se(!1),l(e),z.fromTo(m.userData.uniforms.uSweep,{value:0},{value:1,delay:.5,duration:1.4,ease:"power2.inOut"})))};
const _texScreen = (window.__dluzScreens && window.__dluzScreens[s]) ? window.__dluzScreens[s] : m.map;
const _matPhoneScreen = f.useMemo(() => {
  return new Ae({
    map: _texScreen,
    roughness: 0.08,
    metalness: 0.04,
    clearcoat: 1.0,
    clearcoatRoughness: 0.02
  });
}, [s, _texScreen]);

const _matPhoneBack = f.useMemo(() => {
  return new Ae({
    map: window.__dluzPhoneBack || m.map,
    roughness: 0.35,
    metalness: 0.85,
    clearcoat: 0.8,
    clearcoatRoughness: 0.08
  });
}, []);

const _texLabel = (window.__dluzLabels && window.__dluzLabels[s]) ? window.__dluzLabels[s] : null;
const _matPhoneLabel = f.useMemo(() => {
  return new Ae({
    map: _texLabel,
    transparent: true,
    roughness: 0.15,
    metalness: 0.2,
    clearcoat: 0.8,
    clearcoatRoughness: 0.05
  });
}, [s, _texLabel]);

const _children = [
  n.jsxs("group", { children: [
    // Titanium Body
    n.jsx("mesh", { geometry: _geomPhoneBody, material: _matTitaniumChassis }),
    // Screen (Service UI on front display)
    n.jsx("mesh", { geometry: _geomPhoneScreen, material: _matPhoneScreen, position: [0, 0, 0.042] }),
    // Backplate (Laser etched DLuz Infinity logo)
    n.jsx("mesh", { geometry: _geomPhoneBack, material: _matPhoneBack, position: [0, 0, -0.042], rotation: [0, Math.PI, 0] }),
    // Camera Bump
    n.jsx("mesh", { geometry: _geomPhoneCam, material: _matTitaniumChassis, position: [-0.27, 0.88, -0.058] }),
    // Triple Lens
    n.jsx("mesh", { geometry: _geomPhoneLens, material: _matBlackGlass, position: [-0.19, 0.96, -0.076], rotation: [Math.PI/2, 0, 0] }),
    n.jsx("mesh", { geometry: _geomPhoneLens, material: _matBlackGlass, position: [-0.35, 0.96, -0.076], rotation: [Math.PI/2, 0, 0] }),
    n.jsx("mesh", { geometry: _geomPhoneLens, material: _matBlackGlass, position: [-0.27, 0.80, -0.076], rotation: [Math.PI/2, 0, 0] }),
    // Flash
    n.jsx("mesh", { geometry: _geomPhoneFlash, material: _matFlash, position: [-0.19, 0.80, -0.07], rotation: [Math.PI/2, 0, 0] }),
    // 3D Theme Badge Label under each phone (Front & Back)
    n.jsx("mesh", { geometry: _geomPhoneLabel, material: _matPhoneLabel, position: [0, -1.48, 0.02] }),
    n.jsx("mesh", { geometry: _geomPhoneLabel, material: _matPhoneLabel, position: [0, -1.48, -0.02], rotation: [0, Math.PI, 0] })
  ]})
];
return n.jsxs("group", { ref: r, onPointerOver: w, onPointerOut: _, onClick: A, children: _children });
}function kn(e){return e<.85?{top:ge([0,5.45,-3.5],[-.52,0,0],2.5,-1),bottom:ge([0,-4.95,-1.5],[.42,0,0],2.8,1)}:{top:ge([0,5.55,-4.2],[-.5,0,0],3.4,-1),bottom:ge([0,-5.05,-1.2],[.4,0,0],4.4,1)}}const Sn=2.3;function ge(e,t,o,r){const s=new W(0,r*Sn*o,0).applyEuler(new Dt(...t));return{p:[e[0]-s.x,e[1]-s.y,e[2]-s.z],r:t,s:o}}function Rn({assets:e,aspect:t}){const o=f.useRef(),r=f.useRef(),s=f.useRef(),i=f.useRef(),c=f.useMemo(()=>({alu:at(e.source.alu,{color:"#dfe3e9",rim:.35,roughness:.14,envMapIntensity:1.7}),body:at(e.source.body,{color:"#5a5f68",rim:.5,roughness:.2,envMapIntensity:1.5})}),[e]);f.useEffect(()=>()=>Object.values(c).forEach(m=>m.dispose()),[c]);const u=f.useMemo(()=>kn(t),[t]),l=f.useMemo(()=>({v:0}),[]);f.useEffect(()=>{z.to(l,{v:1,duration:3.2,delay:.1,ease:"expo.out"})},[l]),U(({clock:m})=>{const g=m.elapsedTime,a=b.k*b.k*(3-2*b.k),w=1-l.v+a*1.1,{top:_,bottom:A}=u,{x,y:$}=h.drive;o.current.position.set(_.p[0]+x*.16,_.p[1]+w*5+$*.06+Math.sin(g*.4)*.05,_.p[2]),o.current.rotation.set(_.r[0]+Math.sin(g*.3)*.012+$*.03,_.r[1],_.r[2]-x*.025),s.current.position.set(A.p[0]+x*.2,A.p[1]-w*5+$*.05+Math.sin(g*.35+1)*.04,A.p[2]),s.current.rotation.set(A.r[0]+Math.cos(g*.28)*.01-$*.03,A.r[1],A.r[2]-x*.02),r.current.rotation.y=g*.035+x*.25,i.current.rotation.y=-g*.03+.6+x*.3});const p=()=>null;return n.jsxs(n.Fragment,{children:[n.jsx("group",{ref:o,visible:!1,scale:u.top.s,children:n.jsx("group",{ref:r})}),n.jsx("group",{ref:s,visible:!1,scale:u.bottom.s,children:n.jsx("group",{ref:i})})]})}function Ln(){return n.jsxs(Et,{resolution:512,frames:1,children:[n.jsx("color",{attach:"background",args:["#000"]}),n.jsx(V,{form:"rect",intensity:5,position:[-4.5,.5,6],scale:[1.1,16,1],target:[0,0,0]}),n.jsx(V,{form:"rect",intensity:2.4,position:[5.5,0,5],scale:[.55,16,1],target:[0,0,0]}),n.jsx(V,{form:"rect",intensity:1.2,position:[0,8,3],scale:[10,2,1],target:[0,0,0]}),n.jsx(V,{form:"rect",intensity:3.5,position:[-7,0,-6],scale:[.6,16,1],target:[0,0,0]}),n.jsx(V,{form:"rect",intensity:3.5,position:[7,0,-6],scale:[.6,16,1],target:[0,0,0]}),n.jsx(V,{form:"circle",intensity:.5,position:[0,-8,2],scale:6,target:[0,0,0]})]})}function En(){const e=f.useRef(),t=f.useRef(),o=f.useRef(),r=f.useRef(),s=f.useRef(),i=f.useRef(),c=f.useRef();return U(()=>{const u=1-.75*b.k;i.current.intensity=26*u,c.current.intensity=10*u,r.current.intensity=20*u,s.current.intensity=16*u,e.current.color.copy(h.rim),t.current.color.copy(h.rim),o.current.color.copy(h.rim),r.current.color.copy(h.rim),s.current.color.copy(h.rim)}),n.jsxs(n.Fragment,{children:[n.jsx("ambientLight",{intensity:.04}),n.jsx("directionalLight",{position:[-3,5,8],intensity:.45}),n.jsx("directionalLight",{ref:e,position:[-8,2,-6],intensity:2.6}),n.jsx("directionalLight",{ref:t,position:[8,-1,-6],intensity:2.6}),n.jsx("directionalLight",{ref:o,position:[0,9,-2],intensity:.5}),n.jsx("pointLight",{ref:i,position:[-1.6,3.1,4.6],intensity:26,distance:8,decay:2,color:"#fff4ea"}),n.jsx("pointLight",{ref:c,position:[1.9,1.2,4.2],intensity:10,distance:7,decay:2,color:"#eaf1ff"}),n.jsx("pointLight",{ref:r,position:[0,-3.1,3.4],intensity:20,distance:7,decay:2}),n.jsx("pointLight",{ref:s,position:[0,2.8,-.8],intensity:16,distance:6,decay:2})]})}function Nn(){const e=xe(l=>l.size.width/l.size.height),t=f.useRef(),o=f.useRef(),r=f.useRef(),s=f.useRef(),i=f.useRef(),c=f.useMemo(()=>new Bt,[]),u=f.useMemo(()=>({p:[0,0,0],rx:0,rz:0,s:1,yaw:0}),[]);return U(()=>{const l=b.k;if(l<.001){[t,o,r,s,i].forEach(m=>m.current.intensity=0);return}const p=Be(e,u).p;t.current.position.set(p[0]-4.2,p[1]+2.4,p[2]+5.5),t.current.intensity=70*l,o.current.position.set(p[0]+5,p[1]-.6,p[2]+4.5),o.current.intensity=16*l,r.current.position.set(p[0]-3.4,p[1]+1,p[2]-3),s.current.position.set(p[0]+3.2,p[1]-.5,p[2]-2.6),r.current.color.copy(h.rim),s.current.color.copy(h.rim),r.current.intensity=40*l,s.current.intensity=55*l,i.current.position.set(p[0]-1.2,p[1]+u.s*.4+2.2,p[2]+9),c.position.set(p[0],p[1]+b.focusY*u.s,p[2]+u.s),c.updateMatrixWorld(),i.current.intensity=650*l*b.spot}),n.jsxs(n.Fragment,{children:[n.jsx("pointLight",{ref:t,decay:2,distance:24,color:"#fff6ec"}),n.jsx("pointLight",{ref:o,decay:2,distance:20,color:"#e6eeff"}),n.jsx("pointLight",{ref:r,decay:2,distance:12}),n.jsx("pointLight",{ref:s,decay:2,distance:12}),n.jsx("primitive",{object:c}),n.jsx("spotLight",{ref:i,target:c,angle:.12,penumbra:1,decay:2,distance:30,color:"#ffffff"})]})}function Tn(){const e=xe(o=>o.gl),t=xe(o=>o.size.height);return f.useEffect(()=>on(e.domElement,t),[e,t]),U((o,r)=>{rn(Math.min(r,1/30));const{slotOf:s,ready:i,setActive:c}=P.getState();if(!i)return;const u=s.indexOf(xt()),l=ce(u);c(l),l!==h.lit&&tn()&&(h.lit=l,Te(Y[l]))}),null}function Cn(){return U(({camera:e},t)=>{const o=1-Math.exp(-3*Math.min(t,.03333333333333333)),r=Math.sin(h.kick*Math.PI)*.55,{drive:s}=h;e.position.x+=(-s.x*.35-e.position.x)*o,e.position.y+=(-s.y*.12-e.position.y)*o,e.position.z+=(Ne.z-r-e.position.z)*o,e.lookAt(0,0,0)}),null}const On=Array.from({length:M},(e,t)=>t);function An(){const e=gn(),t=P(s=>s.setReady),o=xe(s=>s.size.width/s.size.height),r=f.useMemo(()=>qt(o),[o]);return f.useEffect(()=>{t()},[t]),n.jsxs(n.Fragment,{children:[n.jsx(Pn,{center:r}),n.jsx(Rn,{assets:e,aspect:o}),On.map(s=>n.jsx(_n,{item:s,assets:e,aspect:o},s))]})}const F=1,Dn=typeof window<"u"&&window.devicePixelRatio||1,In=typeof window<"u"&&window.matchMedia?.("(pointer: coarse)").matches,we=Math.max(F,Math.min(Dn,1.75)),lt=Math.max(F,Math.min(we,In?1.5:1.75)),Bn=e=>Math.max(F,Math.min(we,Math.round(e*4)/4));class Fn extends f.Component{constructor(){super(...arguments);Ge(this,"state",{failed:!1})}static getDerivedStateFromError(){return{failed:!0}}componentDidCatch(o){console.error("[Blazing] 3D scene unavailable:",o),P.getState().setReady()}render(){return this.state.failed?null:this.props.children}}function Yn(){const[e,t]=f.useState(lt),o=f.useCallback(({factor:r})=>t(Bn(F+(we-F)*r)),[]);return n.jsx(Fn,{children:n.jsx(Rt,{className:"hero__canvas",dpr:e,gl:{antialias:!0,powerPreference:"high-performance"},camera:{fov:Ne.fov,position:[0,0,Ne.z],near:.1,far:80},onCreated:({gl:r})=>{r.toneMapping=It,r.toneMappingExposure=1.05},children:n.jsxs(f.Suspense,{fallback:null,children:[n.jsx(Ln,{}),n.jsx(En,{}),n.jsx(Nn,{}),n.jsx(Tn,{}),n.jsx(An,{}),n.jsx(Cn,{}),n.jsx(Lt,{factor:(lt-F)/Math.max(we-F,.001),step:.2,flipflops:4,onChange:o,onFallback:()=>t(F)})]})})})}function ae({text:e,show:t=!0,className:o="",stagger:r=.03,delay:s=0}){const[i,c]=f.useState(e),u=f.useRef(),l=f.useRef(e),p=f.useRef(e),m=f.useRef(!1);l.current=e;const g=()=>u.current.querySelectorAll(".roll__c");return f.useLayoutEffect(()=>{if(!t||m.current||e===p.current)return;m.current=!0;const a=()=>{m.current&&(m.current=!1,l.current===p.current?z.to(g(),{yPercent:0,duration:.6,stagger:r,ease:"expo.out",overwrite:!0}):(p.current=l.current,c(l.current)))};z.to(g(),{yPercent:-110,duration:.34,stagger:r*.5,ease:"power3.in",overwrite:!0,onComplete:a,onInterrupt:a})},[e,i,t,r]),f.useLayoutEffect(()=>{if(!t){z.set(g(),{yPercent:110});return}z.fromTo(g(),{yPercent:110},{yPercent:0,duration:.9,stagger:r,ease:"expo.out",delay:s,overwrite:!0})},[i,t,r,s]),n.jsx("span",{ref:u,className:`roll ${o}`,"aria-label":i,children:[...i].map((a,w)=>n.jsx("span",{className:"roll__m","aria-hidden":"true",children:n.jsx("span",{className:"roll__c",children:a===" "?" ":a})},`${i}-${w}`))})}function ut({id:e,render:t,className:o="",delay:r=0,show:s=!0}){const[i,c]=f.useState(e),u=f.useRef(),l=f.useRef(e),p=f.useRef(e),m=f.useRef(!1);l.current=e;const g=()=>u.current.querySelectorAll("[data-line]");return f.useLayoutEffect(()=>{if(!s||m.current||e===p.current)return;m.current=!0;const a=()=>{m.current&&(m.current=!1,l.current===p.current?z.to(g(),{yPercent:0,opacity:1,duration:.5,stagger:.05,ease:"expo.out",overwrite:!0}):(p.current=l.current,c(l.current)))};z.to(g(),{yPercent:-60,opacity:0,duration:.3,stagger:.03,ease:"power2.in",overwrite:!0,onComplete:a,onInterrupt:a})},[e,i,s]),f.useLayoutEffect(()=>{if(!s){z.set(g(),{yPercent:80,opacity:0});return}z.fromTo(g(),{yPercent:80,opacity:0},{yPercent:0,opacity:1,duration:.85,stagger:.07,ease:"expo.out",delay:r,overwrite:!0})},[i,s,r]),n.jsx("div",{ref:u,className:`swap ${o}`,children:t(i)})}const Ee=e=>String(e).padStart(2,"0"),Hn={bolt:n.jsx("path",{d:"M13.5 2.5 5.5 13.5h6l-1 8 8-11h-6l1-8Z"}),leaf:n.jsxs(n.Fragment,{children:[n.jsx("path",{d:"M5 19c0-8 5-13.5 14-14-.5 9-6 14-14 14Z"}),n.jsx("path",{d:"M5 19 13 11"})]}),cube:n.jsxs(n.Fragment,{children:[n.jsx("path",{d:"m12 3 8 4.5v9L12 21l-8-4.5v-9L12 3Z"}),n.jsx("path",{d:"m4 7.5 8 4.5 8-4.5M12 12v9"})]}),hex:n.jsxs(n.Fragment,{children:[n.jsx("path",{d:"m12 2.8 8 4.6v9.2l-8 4.6-8-4.6V7.4l8-4.6Z"}),n.jsx("path",{d:"M10 8.5h2.6a1.7 1.7 0 0 1 0 3.4H10m0 0h3a1.8 1.8 0 0 1 0 3.6h-3V8.5Z"})]})};function qn({name:e}){return n.jsx("svg",{viewBox:"0 0 24 24","aria-hidden":"true",className:"bn__icon",children:Hn[e]})}function Un(){const e=P(a=>a.mode),t=P(a=>a.active),o=P(a=>a.benefit),r=P(a=>a.setBenefit),s=P(a=>a.closeDetail),i=e==="detail",c=Y[t],u=o>=0?q[o]:null,l=u?u.title:["DLuz Digital",c.name],p=u?u.id:`flavor-${c.id}`,[m,g]=f.useState(0);return f.useEffect(()=>{i&&g(a=>a+1)},[i]),n.jsxs("section",{className:`detail ${i?"is-open":""}`,"aria-hidden":!i,"aria-label":"Product details",children:[n.jsxs("button",{className:"detail__close",type:"button",onClick:s,tabIndex:i?0:-1,children:[n.jsx("span",{className:"detail__x","aria-hidden":"true"}),n.jsx("span",{children:"Voltar às Soluções"})]}),n.jsxs("div",{className:"detail__copy",children:[n.jsx(ut,{id:p,show:m>0,delay:.35,className:"detail__eyebrow",render:a=>{const w=q.find(_=>_.id===a);return w?n.jsxs("p",{"data-line":!0,className:"cmp",children:[n.jsx("span",{className:"cmp__label",children:w.label}),n.jsx("span",{className:"cmp__x","aria-hidden":"true",children:"×"}),n.jsx("s",{className:"cmp__struck",children:w.crossedOut})]}):n.jsxs("p",{"data-line":!0,className:"eyebrow detail__meta",children:[n.jsx("span",{className:"dot"})," N° ",Ee(t+1)," — Alta Performance & ROI Garantido"]})}}),n.jsx("h2",{className:"detail__title",children:l.map((a,w)=>n.jsx("span",{className:"detail__line",children:n.jsx(ae,{text:a,show:m>0,stagger:.028,delay:.25+w*.08})},w))}),n.jsx(ut,{id:p,show:m>0,delay:.55,className:"detail__body",render:a=>{const w=q.find(_=>_.id===a);return n.jsx("p",{"data-line":!0,children:w?w.description:c.description})}}),n.jsx("p",{className:"detail__count eyebrow",children:u?`${Ee(o+1)} / ${Ee(q.length)}`:c.notes})]},m),n.jsx("nav",{className:"detail__benefits","aria-label":"Product benefits",children:q.map((a,w)=>n.jsxs("button",{type:"button",className:`bn ${w===o?"is-active":""}`,onClick:()=>r(w),"aria-pressed":w===o,tabIndex:i?0:-1,style:{"--i":w},children:[n.jsx(qn,{name:a.icon}),n.jsx("span",{className:"bn__label",children:a.title.join(" ")})]},a.id))})]})}const Oe=e=>String(e).padStart(2,"0"),$n=8;function Pt({className:e}){return n.jsx("svg",{className:e,viewBox:"0 0 24 32","aria-hidden":"true",children:n.jsx("path",{d:"M12.6 0c1.2 5.3 7.9 8.9 7.9 17.1A8.5 8.5 0 0 1 3.5 17c0-4 1.9-6.5 4-8.4-.1 3 1.1 5.1 3.5 6C10 10.2 10.8 4.3 12.6 0Zm-.3 20.3c-.4 2.2-2.6 3-2.6 5.4a2.7 2.7 0 0 0 5.4.1c0-2.3-2.2-3.2-2.8-5.5Z"})})}
function Xn(){
  return n.jsxs("header",{className:"hud__top",children:[
    n.jsxs("a",{className:"brand",href:"index.html","aria-label":"DLuz Digital — Início",children:[
      n.jsx("img",{src:"assets/dluz_infinity.png",alt:"DLuz Digital",style:{height:"30px",width:"auto",marginRight:"10px",filter:"drop-shadow(0 0 10px rgba(16,185,129,0.45))"}}),
      n.jsxs("div",{className:"brand__text",style:{display:"flex",flexDirection:"column",gap:"2px"},children:[
        n.jsxs("div",{style:{display:"flex",alignItems:"baseline",gap:"5px",lineHeight:"1.1"},children:[
          n.jsx("span",{className:"brand__word",children:"DLuz"}),
          n.jsx("span",{className:"brand__sub",children:"Digital"})
        ]}),
        n.jsx("span",{className:"brand__tagline",children:"MARKETING DIGITAL"})
      ]})
    ]}),
    n.jsxs("nav",{className:"nav","aria-label":"Primary",children:[
      n.jsxs("a",{href:"#solucoes",children:[n.jsx("sup",{children:"01"}),"Soluções 3D"]}),
      n.jsxs("a",{href:"metodologia.html",children:[n.jsx("sup",{children:"02"}),"Metodologia"]}),
      n.jsxs("a",{href:"resultados.html",children:[n.jsx("sup",{children:"03"}),"Resultados"]}),
      n.jsxs("a",{href:"equipe.html",children:[n.jsx("sup",{children:"04"}),"Equipe"]})
    ]}),
    n.jsxs("div",{className:"hud__actions",children:[
      n.jsx("a",{className:"link",href:"contato.html",children:"Contato"}),
      n.jsxs("a",{className:"menu",href:"menu.html","aria-label":"Abrir menu",children:[
        n.jsx("span",{children:"Menu"}),
        n.jsx("i",{})
      ]})
    ]})
  ]});
}
function Vn({active:e,ready:t}){const o=P(l=>l.goTo),r=P(l=>l.hovered),s=f.useRef(null),i=P(l=>l.mode),c=f.useRef({hover:!1,drag:!1,detail:!1}),u=()=>{const l=s.current;l&&(c.current.hover||c.current.drag||c.current.detail?l.pause():l.resume())};return f.useEffect(()=>{if(!t||window.matchMedia("(prefers-reduced-motion: reduce)").matches)return;const l=document.querySelector(`[data-seg="${e}"]`),p={p:0},m=z.to(p,{p:1,duration:$n,delay:1.4,ease:"none",onUpdate:()=>l.style.setProperty("--p",p.p),onComplete:()=>P.getState().step(1)});return s.current=m,u(),()=>{m.kill(),l.style.setProperty("--p",0)}},[e,t]),f.useEffect(()=>{c.current.hover=r!==null,u()},[r]),f.useEffect(()=>{c.current.detail=i==="detail",u()},[i]),f.useEffect(()=>nn(l=>{c.current.drag=l,u()}),[]),n.jsx("div",{className:"progress",role:"tablist","aria-label":"Escolha uma solução",children:Y.map((l,p)=>n.jsxs("button",{type:"button",role:"tab","aria-selected":p===e,className:`seg ${p===e?"is-active":""} ${p===r?"is-hover":""}`,onClick:()=>o(p),"data-seg":p,children:[n.jsx("span",{className:"seg__label",children:l.name}),n.jsx("span",{className:"seg__track",children:n.jsx("span",{className:"seg__fill"})})]},l.id))})}function Zn({ready:e}){const{progress:t}=Nt();return n.jsx("div",{className:`loader ${e?"is-done":""}`,"aria-hidden":e,children:n.jsxs("div",{className:"loader__inner",children:[n.jsx(Pt,{className:"loader__flame"}),n.jsx("span",{className:"loader__pct",children:Oe(Math.round(t))})]})})}function Wn(){const e=P(s=>s.active),t=P(s=>s.ready),o=P(s=>s.mode),r=Y[e];return f.useEffect(()=>{const s=i=>{const c=P.getState();if(c.mode==="detail"){i.key==="Escape"&&c.closeDetail(),(i.key==="ArrowDown"||i.key==="ArrowRight")&&c.setBenefit(c.benefit+1),(i.key==="ArrowUp"||i.key==="ArrowLeft")&&c.setBenefit(c.benefit-1);return}i.key==="ArrowRight"&&c.step(1),i.key==="ArrowLeft"&&c.step(-1)};return window.addEventListener("keydown",s),()=>window.removeEventListener("keydown",s)},[]),n.jsxs(n.Fragment,{children:[n.jsx(Zn,{ready:t}),n.jsxs("div",{className:`hud ${t?"is-ready":""} ${o==="detail"?"is-detail":""}`,children:[n.jsx(Xn,{}),n.jsxs("div",{className:"title",children:[n.jsxs("p",{className:"eyebrow title__eyebrow",children:[n.jsx("span",{className:"dot"})," Solução Executiva — IA & Performance"]}),n.jsxs("h1",{className:"title__name",children:[n.jsx("span",{className:"sr-only",children:"DLuz Digital — "}),n.jsx(ae,{text:r.name,show:t,stagger:.04,delay:.4})]}),n.jsx("p",{className:"title__line",children:n.jsx(ae,{text:r.line,show:t,stagger:.012,delay:.6})})]}),n.jsxs("footer",{className:"hud__bottom",children:[n.jsxs("div",{className:"meta",children:[n.jsxs("div",{className:"index",children:[n.jsx("span",{className:"index__now",children:n.jsx(ae,{text:Oe(e+1),show:t,stagger:.05,delay:.3})}),n.jsx("span",{className:"index__sep"}),n.jsx("span",{className:"index__total",children:Oe(Y.length)})]}),n.jsx("p",{className:"meta__notes",children:n.jsx(ae,{text:r.notes,show:t,stagger:.006,delay:.5})})]}),n.jsx(Vn,{active:e,ready:t}),n.jsxs("div",{className:"scroll",children:[n.jsx("span",{children:"Scroll to discover"}),n.jsx("i",{className:"scroll__line"})]})]}),n.jsx(Un,{})]})]})}function Kn(){return n.jsxs("main",{className:"hero",children:[n.jsx(Yn,{}),n.jsx(Wn,{}),n.jsx("div",{className:"floor-glow","aria-hidden":"true"})]})}Tt.createRoot(document.getElementById("root")).render(n.jsx(f.StrictMode,{children:n.jsx(Kn,{})}));
