import os, sqlite3, json

site_dir = r"c:\Users\dluzgg\Documents\antigravity\serene-newton\prospector-de-sites\dashboard\sites\implantus-centro-odontologico"
os.makedirs(site_dir, exist_ok=True)

html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Implantus Centro Odontológico — Paraíso do Tocantins - TO</title>
    <meta name="description" content="Recupere a segurança de sorrir e mastigar sem medo. Implantes dentários, ortodontia e reabilitação oral com tecnologia e conforto em Paraíso do Tocantins.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #0F384C;
            --primary-light: #18526B;
            --accent: #C99757;
            --accent-hover: #B88544;
            --accent-soft: #F9F4ED;
            --dark: #1A242B;
            --muted: #64748B;
            --bg: #F8FAFC;
            --card-bg: #FFFFFF;
            --line: #E2E8F0;
            --success: #10B981;
            --sans: 'Plus Jakarta Sans', -apple-system, sans-serif;
            --serif: 'Playfair Display', Georgia, serif;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body { font-family: var(--sans); color: var(--dark); background: var(--bg); line-height: 1.6; overflow-x: hidden; }

        .container { width: 100%; max-width: 1200px; margin: 0 auto; padding: 0 24px; }

        /* Top Notification */
        .top-notice { background: var(--primary); color: #E2F0F7; font-size: 13px; text-align: center; padding: 8px 16px; font-weight: 500; display: flex; justify-content: center; align-items: center; gap: 8px; }
        .top-notice span.badge { background: var(--accent); color: #fff; padding: 2px 8px; border-radius: 4px; font-weight: 700; font-size: 11px; }

        /* Navbar */
        nav { background: #fff; border-bottom: 1px solid var(--line); position: sticky; top: 0; z-index: 100; }
        .nav-inner { display: flex; justify-content: space-between; align-items: center; height: 80px; }
        .brand { text-decoration: none; display: flex; flex-direction: column; }
        .brand-title { font-family: var(--serif); font-size: 24px; font-weight: 700; color: var(--primary); letter-spacing: -0.5px; }
        .brand-subtitle { font-size: 10px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: var(--accent); }
        .nav-links { display: flex; gap: 28px; list-style: none; align-items: center; }
        .nav-links a { color: var(--muted); text-decoration: none; font-size: 14px; font-weight: 600; transition: color .2s; }
        .nav-links a:hover { color: var(--primary); }
        .btn-nav { background: var(--accent); color: #fff !important; padding: 10px 20px; border-radius: 8px; font-weight: 700 !important; transition: background .2s !important; display: inline-flex; align-items: center; gap: 8px; }
        .btn-nav:hover { background: var(--accent-hover) !important; }

        /* Hero */
        .hero { padding: 70px 0 80px; background: linear-gradient(180deg, #FFFFFF 0%, #F1F6F9 100%); border-bottom: 1px solid var(--line); }
        .hero-grid { display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 48px; align-items: center; }
        .hero-kicker { display: inline-flex; align-items: center; gap: 8px; background: var(--accent-soft); color: var(--accent-hover); padding: 6px 14px; border-radius: 30px; font-size: 12px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 18px; border: 1px solid rgba(201,151,87,0.3); }
        .hero h1 { font-family: var(--serif); font-size: clamp(34px, 4.2vw, 52px); line-height: 1.15; color: var(--primary); font-weight: 700; margin-bottom: 20px; letter-spacing: -0.5px; }
        .hero h1 em { font-style: normal; color: var(--accent); }
        .hero-desc { font-size: 18px; color: var(--muted); margin-bottom: 32px; max-width: 540px; }
        .hero-actions { display: flex; flex-wrap: wrap; gap: 16px; align-items: center; margin-bottom: 36px; }
        .btn-primary { background: #25D366; color: #fff; text-decoration: none; padding: 16px 32px; border-radius: 10px; font-size: 16px; font-weight: 700; display: inline-flex; align-items: center; gap: 10px; box-shadow: 0 8px 24px rgba(37,211,102,0.3); transition: transform .2s, box-shadow .2s; }
        .btn-primary:hover { transform: translateY(-2px); box-shadow: 0 12px 30px rgba(37,211,102,0.4); }
        .btn-secondary { background: #fff; color: var(--primary); text-decoration: none; padding: 16px 24px; border-radius: 10px; font-size: 15px; font-weight: 700; border: 1px solid var(--line); transition: border-color .2s; }
        .btn-secondary:hover { border-color: var(--primary); }

        .trust-badge { display: flex; align-items: center; gap: 14px; padding-top: 24px; border-top: 1px solid var(--line); }
        .stars { color: #F59E0B; font-size: 18px; letter-spacing: 2px; }
        .trust-text { font-size: 13px; color: var(--muted); line-height: 1.4; }
        .trust-text strong { color: var(--dark); }

        .hero-card { background: #fff; border-radius: 20px; padding: 28px; border: 1px solid var(--line); box-shadow: 0 20px 40px rgba(15,56,76,0.08); position: relative; }
        .hero-card-img { width: 100%; height: 320px; background: linear-gradient(135deg, #0F384C 0%, #1A546F 100%); border-radius: 14px; display: flex; flex-direction: column; align-items: center; justify-content: center; color: #fff; text-align: center; padding: 24px; }
        .hero-card-img svg { width: 64px; height: 64px; fill: var(--accent); margin-bottom: 16px; }
        .hero-card-floating { position: absolute; bottom: 10px; left: -10px; right: -10px; background: #fff; padding: 16px 20px; border-radius: 14px; border: 1px solid var(--line); box-shadow: 0 10px 25px rgba(0,0,0,0.08); display: flex; align-items: center; justify-content: space-between; }
        .floating-stat { font-family: var(--serif); font-size: 26px; font-weight: 700; color: var(--primary); }
        .floating-label { font-size: 12px; color: var(--muted); font-weight: 600; }

        /* Social Strip */
        .social-strip { padding: 40px 0; background: #fff; border-bottom: 1px solid var(--line); }
        .strip-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 24px; text-align: center; }
        .strip-item h4 { font-family: var(--serif); font-size: 32px; color: var(--primary); margin-bottom: 4px; }
        .strip-item p { font-size: 14px; color: var(--muted); font-weight: 500; }

        /* Services */
        .services { padding: 90px 0; }
        .section-header { text-align: center; max-width: 680px; margin: 0 auto 56px; }
        .section-kicker { font-size: 12px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: var(--accent); margin-bottom: 10px; }
        .section-title { font-family: var(--serif); font-size: clamp(28px, 3.2vw, 42px); color: var(--primary); line-height: 1.2; margin-bottom: 14px; }
        .section-desc { font-size: 16px; color: var(--muted); }

        .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 28px; }
        .service-card { background: #fff; border: 1px solid var(--line); border-radius: 16px; padding: 36px 30px; transition: transform .25s, box-shadow .25s, border-color .25s; display: flex; flex-direction: column; }
        .service-card:hover { transform: translateY(-4px); box-shadow: 0 16px 32px rgba(15,56,76,0.08); border-color: var(--accent); }
        .service-icon { width: 52px; height: 52px; border-radius: 12px; background: var(--accent-soft); display: flex; align-items: center; justify-content: center; color: var(--accent-hover); font-size: 22px; margin-bottom: 22px; font-weight: 700; }
        .service-card h3 { font-family: var(--serif); font-size: 22px; color: var(--primary); margin-bottom: 12px; }
        .service-card p { font-size: 15px; color: var(--muted); margin-bottom: 24px; flex-grow: 1; line-height: 1.6; }
        .service-link { color: var(--accent); font-size: 14px; font-weight: 700; text-decoration: none; display: inline-flex; align-items: center; gap: 6px; }
        .service-link:hover { color: var(--accent-hover); }

        /* Testimonials */
        .testimonials { padding: 90px 0; background: #fff; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); }
        .testi-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; }
        .testi-card { background: var(--bg); border: 1px solid var(--line); border-radius: 16px; padding: 32px; display: flex; flex-direction: column; justify-content: space-between; }
        .testi-stars { color: #F59E0B; margin-bottom: 14px; font-size: 16px; }
        .testi-quote { font-size: 15px; color: var(--dark); font-style: italic; line-height: 1.6; margin-bottom: 20px; }
        .testi-author { display: flex; align-items: center; gap: 12px; }
        .testi-avatar { width: 42px; height: 42px; border-radius: 50%; background: var(--primary); color: #fff; font-weight: 700; display: flex; align-items: center; justify-content: center; font-size: 15px; }
        .testi-name { font-weight: 700; font-size: 14px; color: var(--primary); }
        .testi-role { font-size: 12px; color: var(--muted); }

        /* Location */
        .location-section { padding: 80px 0; }
        .location-box { background: var(--primary); color: #fff; border-radius: 24px; padding: 60px 48px; display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center; }
        .location-box h2 { font-family: var(--serif); font-size: 36px; margin-bottom: 16px; color: #fff; }
        .location-box p { color: #CBD5E1; font-size: 16px; margin-bottom: 28px; }
        .info-list { list-style: none; margin-bottom: 32px; }
        .info-list li { margin-bottom: 14px; display: flex; align-items: flex-start; gap: 12px; font-size: 15px; color: #E2E8F0; }
        .info-list strong { color: #fff; }

        /* Floating WhatsApp Button */
        .float-wa { position: fixed; bottom: 28px; right: 28px; z-index: 999; background: #25D366; color: #fff; width: 62px; height: 62px; border-radius: 50%; display: flex; align-items: center; justify-content: center; text-decoration: none; box-shadow: 0 10px 25px rgba(37,211,102,0.4); transition: transform .25s; }
        .float-wa:hover { transform: scale(1.1); }
        .float-wa svg { width: 34px; height: 34px; fill: currentColor; }

        /* Footer */
        footer { background: #0A2633; color: #94A3B8; padding: 48px 0 32px; font-size: 14px; border-top: 1px solid rgba(255,255,255,0.08); }
        .footer-grid { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px; margin-bottom: 32px; }
        .footer-copy { text-align: center; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 24px; font-size: 12px; }

        @media (max-width: 900px) {
            .hero-grid { grid-template-columns: 1fr; text-align: center; }
            .hero-desc { margin: 0 auto 32px; }
            .hero-actions { justify-content: center; }
            .trust-badge { justify-content: center; }
            .hero-card { max-width: 440px; margin: 0 auto; }
            .location-box { grid-template-columns: 1fr; padding: 40px 24px; text-align: center; }
            .info-list li { justify-content: center; }
            .nav-links { display: none; }
        }
    </style>
</head>
<body>

    <div class="top-notice">
        <span class="badge">PARAÍSO DO TOCANTINS</span>
        Atendimento com hora marcada e avaliação individualizada · Av. Bernardo Sayão
    </div>

    <nav>
        <div class="container nav-inner">
            <a href="#" class="brand">
                <span class="brand-title">Implantus</span>
                <span class="brand-subtitle">CENTRO ODONTOLÓGICO</span>
            </a>
            <ul class="nav-links">
                <li><a href="#especialidades">Especialidades</a></li>
                <li><a href="#depoimentos">Avaliações</a></li>
                <li><a href="#localizacao">Onde Estamos</a></li>
                <li><a href="https://wa.me/5563984812000?text=Olá!%20Gostaria%20de%20agendar%20uma%20avaliação%20na%20Implantus." class="btn-nav" target="_blank">Agendar Consulta</a></li>
            </ul>
        </div>
    </nav>

    <header class="hero">
        <div class="container hero-grid">
            <div>
                <div class="hero-kicker">Odontologia de Alta Precisão em Paraíso</div>
                <h1>Recupere a segurança de sorrir e mastigar <em>sem medo</em></h1>
                <p class="hero-desc">Implantes modernos, reabilitação oral e odontologia estética. O padrão de tecnologia e conforto que o seu sorriso merece, no coração de Paraíso do Tocantins.</p>
                <div class="hero-actions">
                    <a href="https://wa.me/5563984812000?text=Olá!%20Gostaria%20de%20agendar%20uma%20avaliação%20para%20implantes/tratamento." class="btn-primary" target="_blank">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 15 3.8 13.47 3.8 11.91C3.81 7.37 7.5 3.67 12.05 3.67Z"/></svg>
                        Agendar Avaliação no WhatsApp
                    </a>
                    <a href="tel:6336022020" class="btn-secondary">(63) 3602-2020</a>
                </div>
                <div class="trust-badge">
                    <div class="stars">★★★★★</div>
                    <div class="trust-text">
                        <strong>4.9 de 5.0 no Google</strong> · 38 pacientes atendidos e satisfeitos em Paraíso do Tocantins
                    </div>
                </div>
            </div>
            <div class="hero-card">
                <div class="hero-card-img">
                    <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14.5v-9l6 4.5-6 4.5z"/></svg>
                    <h3 style="font-family: var(--serif); font-size: 22px; margin-bottom: 6px;">Tecnologia & Conforto</h3>
                    <p style="font-size: 13px; color: #CBD5E1;">Ambiente moderno preparado para procedimentos sem dor e com recuperação rápida.</p>
                </div>
                <div class="hero-card-floating">
                    <div>
                        <div class="floating-stat">100%</div>
                        <div class="floating-label">Saúde & Bem-Estar Oral</div>
                    </div>
                    <div>
                        <div class="floating-stat" style="color: var(--accent);">38+</div>
                        <div class="floating-label">Avaliações 5 Estrelas</div>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <section class="social-strip">
        <div class="container strip-grid">
            <div class="strip-item">
                <h4>Implantes</h4>
                <p>Materiais de titânio de alta biocompatibilidade</p>
            </div>
            <div class="strip-item">
                <h4>Ortodontia</h4>
                <p>Alinhamento estético rápido e confortável</p>
            </div>
            <div class="strip-item">
                <h4>Segurança</h4>
                <p>Biossegurança rigorosa e planejamento digital</p>
            </div>
            <div class="strip-item">
                <h4>Localização</h4>
                <p>Fácil acesso na Av. Bernardo Sayão</p>
            </div>
        </div>
    </section>

    <section class="services" id="especialidades">
        <div class="container">
            <div class="section-header">
                <div class="section-kicker">Tratamentos Especializados</div>
                <h2 class="section-title">Soluções completas para devolver a função e a estética do seu sorriso</h2>
                <p class="section-desc">Desde a reposição de dentes perdidos até o alinhamento e clareamento, cada etapa é pensada com precisão clínica.</p>
            </div>

            <div class="services-grid">
                <div class="service-card">
                    <div class="service-icon">🦷</div>
                    <h3>Implantes Dentários</h3>
                    <p>Substitua dentes perdidos com estabilidade definitiva. Mastigue qualquer alimento com firmeza e recupere a estética natural do seu sorriso.</p>
                    <a href="https://wa.me/5563984812000?text=Olá!%20Gostaria%20de%20saber%20mais%20sobre%20implantes%20dentários." class="service-link" target="_blank">Saber sobre implantes →</a>
                </div>

                <div class="service-card">
                    <div class="service-icon">✨</div>
                    <h3>Reabilitação Oral & Próteses</h3>
                    <p>Planejamento completo para casos complexos. Próteses fixas sobre implante (protocolo) ou unitárias com encaixe perfeito e alta durabilidade.</p>
                    <a href="https://wa.me/5563984812000?text=Olá!%20Quero%20saber%20sobre%20reabilitação%20oral." class="service-link" target="_blank">Consultar reabilitação →</a>
                </div>

                <div class="service-card">
                    <div class="service-icon">📐</div>
                    <h3>Ortodontia & Aparelhos</h3>
                    <p>Aparelhos modernos e discretos para correção de mordida e alinhamento dos dentes em crianças, jovens e adultos.</p>
                    <a href="https://wa.me/5563984812000?text=Olá!%20Gostaria%20de%20saber%20sobre%20aparelhos%20ortodônticos." class="service-link" target="_blank">Saber sobre ortodontia →</a>
                </div>

                <div class="service-card">
                    <div class="service-icon">💎</div>
                    <h3>Estética & Clareamento</h3>
                    <p>Lentes de contato dental, facetas em resina e clareamento dental seguro para um sorriso iluminado e harmônico com seu rosto.</p>
                    <a href="https://wa.me/5563984812000?text=Olá!%20Quero%20saber%20sobre%20clareamento%20e%20lentes." class="service-link" target="_blank">Ver tratamentos estéticos →</a>
                </div>

                <div class="service-card">
                    <div class="service-icon">🛡️</div>
                    <h3>Prevenção & Profilaxia</h3>
                    <p>Limpeza profunda, remoção de tártaro e acompanhamento periódico para garantir que gengivas e dentes fiquem livres de inflamações.</p>
                    <a href="https://wa.me/5563984812000?text=Olá!%20Quero%20agendar%20uma%20limpeza/revisão." class="service-link" target="_blank">Agendar limpeza →</a>
                </div>

                <div class="service-card">
                    <div class="service-icon">🩺</div>
                    <h3>Avaliação Clínica Completa</h3>
                    <p>Diagnóstico completo com radiografias e fotos intraorais para explicar em detalhes o melhor plano de tratamento para o seu caso.</p>
                    <a href="https://wa.me/5563984812000?text=Olá!%20Quero%20fazer%20uma%20avaliação%20completa." class="service-link" target="_blank">Marcar avaliação →</a>
                </div>
            </div>
        </div>
    </section>

    <section class="testimonials" id="depoimentos">
        <div class="container">
            <div class="section-header">
                <div class="section-kicker">Prova Social no Google</div>
                <h2 class="section-title">O que os pacientes de Paraíso do Tocantins dizem</h2>
                <p class="section-desc">Reputação construída com pontualidade, carinho e resultados transformadores.</p>
            </div>

            <div class="testi-grid">
                <div class="testi-card">
                    <div>
                        <div class="testi-stars">★★★★★</div>
                        <p class="testi-quote">“Clínica impecável! Fiz meu implante com a equipe da Implantus e foi muito mais tranquilo do que eu imaginava. Zero dor e hoje mastigo com total confiança.”</p>
                    </div>
                    <div class="testi-author">
                        <div class="testi-avatar">M</div>
                        <div>
                            <div class="testi-name">Marcos V.</div>
                            <div class="testi-role">Paciente em Paraíso do Tocantins</div>
                        </div>
                    </div>
                </div>

                <div class="testi-card">
                    <div>
                        <div class="testi-stars">★★★★★</div>
                        <p class="testi-quote">“Atendimento excepcional desde a recepção até a cadeira do dentista. Explicaram cada detalhe do meu tratamento ortodôntico. Recomendo para toda a família!”</p>
                    </div>
                    <div class="testi-author">
                        <div class="testi-avatar">A</div>
                        <div>
                            <div class="testi-name">Ana Paula R.</div>
                            <div class="testi-role">Paciente em Paraíso do Tocantins</div>
                        </div>
                    </div>
                </div>

                <div class="testi-card">
                    <div>
                        <div class="testi-stars">★★★★★</div>
                        <p class="testi-quote">“Consultório muito limpo, moderno e com profissionais que realmente transmitem segurança. Nota 10 em pontualidade e atenção aos detalhes.”</p>
                    </div>
                    <div class="testi-author">
                        <div class="testi-avatar">C</div>
                        <div>
                            <div class="testi-name">Carlos E. Silva</div>
                            <div class="testi-role">Paciente em Paraíso do Tocantins</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="location-section" id="localizacao">
        <div class="container">
            <div class="location-box">
                <div>
                    <h2>Venha nos fazer uma visita</h2>
                    <p>Estamos em localização privilegiada no Centro de Paraíso do Tocantins, com estacionamento acessível e ambiente climatizado.</p>
                    <ul class="info-list">
                        <li>📍 <strong>Endereço:</strong> Av. Bernardo Sayão, Centro — Paraíso do Tocantins - TO</li>
                        <li>📞 <strong>Telefone Fixo:</strong> (63) 3602-2020</li>
                        <li>💬 <strong>WhatsApp:</strong> (63) 98481-2000</li>
                        <li>⏰ <strong>Horário:</strong> Segunda a Sexta, das 08h às 18h</li>
                    </ul>
                    <a href="https://wa.me/5563984812000?text=Olá!%20Gostaria%20de%20saber%20como%20chegar%20à%20clínica." class="btn-primary" target="_blank">Falar com a Recepção no WhatsApp</a>
                </div>
                <div style="background: #fff; border-radius: 16px; padding: 24px; color: var(--dark); text-align: left;">
                    <h3 style="font-family: var(--serif); font-size: 20px; color: var(--primary); margin-bottom: 12px;">Como funciona a sua primeira consulta:</h3>
                    <p style="font-size: 14px; color: var(--muted); margin-bottom: 16px;">1. Conversa inicial para entender suas queixas e desejos.</p>
                    <p style="font-size: 14px; color: var(--muted); margin-bottom: 16px;">2. Exame clínico detalhado e fotos em alta definição.</p>
                    <p style="font-size: 14px; color: var(--muted); margin-bottom: 16px;">3. Apresentação clara das opções de tratamento e cronograma.</p>
                    <div style="background: var(--accent-soft); padding: 12px 16px; border-radius: 8px; font-size: 13px; color: var(--accent-hover); font-weight: 600;">
                        ✓ Sem surpresas: você decide com clareza cada etapa.
                    </div>
                </div>
            </div>
        </div>
    </section>

    <a href="https://wa.me/5563984812000?text=Olá!%20Gostaria%20de%20agendar%20uma%20avaliação%20na%20Implantus." class="float-wa" target="_blank" title="Falar no WhatsApp">
        <svg viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 15 3.8 13.47 3.8 11.91C3.81 7.37 7.5 3.67 12.05 3.67Z"/></svg>
    </a>

    <footer>
        <div class="container">
            <div class="footer-grid">
                <div>
                    <h4 style="color: #fff; font-family: var(--serif); font-size: 20px;">Implantus Centro Odontológico</h4>
                    <p style="font-size: 13px; margin-top: 4px;">Excelência em implantes, estética e ortodontia em Paraíso do Tocantins - TO</p>
                </div>
                <div style="font-size: 13px;">
                    Av. Bernardo Sayão, Centro · Tel: (63) 3602-2020
                </div>
            </div>
            <div class="footer-copy">
                © 2026 Implantus Centro Odontológico. Todos os direitos reservados.
            </div>
        </div>
    </footer>

</body>
</html>"""

# Salvar o site principal
with open(os.path.join(site_dir, 'implantus-centro-odontologico.html'), 'w', encoding='utf-8') as f:
    f.write(html_content)

# Salvar a versão editável (editor visual)
editor_block = """<!-- PROSPECTOR-EDITOR-START -->
<style id="pe-style">
#pe-bar{position:fixed;top:0;left:0;right:0;z-index:99999;background:#111;color:#fff;font:14px/1 -apple-system,Segoe UI,Roboto,sans-serif;display:flex;align-items:center;gap:16px;padding:10px 16px;box-shadow:0 2px 8px rgba(0,0,0,.3)}
#pe-bar button{background:#22c55e;color:#fff;border:0;border-radius:8px;padding:8px 16px;font-weight:600;cursor:pointer}
#pe-bar button:hover{background:#16a34a}
body{margin-top:44px !important}
.pe-hover{outline:2px dashed #22c55e !important;outline-offset:2px;cursor:pointer}
[contenteditable="true"]:focus{outline:2px solid #3b82f6 !important;outline-offset:2px}
</style>
<div id="pe-bar">
  <strong>Modo Edição Visual</strong>
  <span>Clique em textos para alterar · clique em imagens para substituir</span>
  <button id="pe-export" type="button">Exportar Página Limpa</button>
</div>
<input type="file" id="pe-file" accept="image/*" style="display:none">
<script id="pe-script">
(function(){
  var TEXT='h1,h2,h3,h4,h5,h6,p,li,a,span,button,td,th,figcaption,blockquote,strong,em';
  document.querySelectorAll(TEXT).forEach(function(el){
    if(el.closest('#pe-bar'))return;
    if(el.children.length===0||el.childElementCount<=1){
      el.addEventListener('click',function(e){
        if(el.tagName==='A'||el.tagName==='BUTTON')e.preventDefault();
        el.setAttribute('contenteditable','true');el.focus();
      });
      el.addEventListener('mouseenter',function(){el.classList.add('pe-hover')});
      el.addEventListener('mouseleave',function(){el.classList.remove('pe-hover')});
      el.addEventListener('blur',function(){el.removeAttribute('contenteditable')});
    }
  });
  var fileInput=document.getElementById('pe-file'),currentImg=null;
  document.querySelectorAll('img').forEach(function(img){
    img.addEventListener('click',function(e){e.preventDefault();e.stopPropagation();currentImg=img;fileInput.click()});
    img.addEventListener('mouseenter',function(){img.classList.add('pe-hover')});
    img.addEventListener('mouseleave',function(){img.classList.remove('pe-hover')});
  });
  fileInput.addEventListener('change',function(){
    var f=fileInput.files[0];if(!f||!currentImg)return;
    var r=new FileReader();
    r.onload=function(){currentImg.src=r.result;if(currentImg.srcset)currentImg.removeAttribute('srcset')};
    r.readAsDataURL(f);fileInput.value='';
  });
  document.getElementById('pe-export').addEventListener('click',function(){
    var doc=document.documentElement.cloneNode(true);
    ['#pe-bar','#pe-style','#pe-script','#pe-file'].forEach(function(s){var n=doc.querySelector(s);if(n)n.remove()});
    doc.querySelectorAll('[contenteditable]').forEach(function(n){n.removeAttribute('contenteditable')});
    doc.querySelectorAll('.pe-hover').forEach(function(n){n.classList.remove('pe-hover')});
    var html='<!DOCTYPE html>\\n'+doc.outerHTML;
    var blob=new Blob([html],{type:'text/html'});
    var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='implantus-centro-odontologico.html';a.click();
  });
})();
</script>
<!-- PROSPECTOR-EDITOR-END -->
</body>"""

editor_html = html_content.replace('</body>', editor_block)
with open(os.path.join(site_dir, 'implantus-centro-odontologico-editor.html'), 'w', encoding='utf-8') as f:
    f.write(editor_html)

# Atualizar status no SQLite
db_path = r"c:\Users\dluzgg\Documents\antigravity\serene-newton\prospector-de-sites\dashboard\prospector.db"
conn = sqlite3.connect(db_path)
conn.execute("UPDATE leads SET status='redesenhado', atualizado=datetime('now','localtime') WHERE slug='implantus-centro-odontologico'")
conn.commit()

# Atualizar dashboard.html estático
conn.row_factory = sqlite3.Row
todos = [dict(r) for r in conn.execute('SELECT * FROM leads ORDER BY atualizado DESC').fetchall()]
conn.close()

dash_dir = r"c:\Users\dluzgg\Documents\antigravity\serene-newton\prospector-de-sites\dashboard"
template_path = os.path.join(dash_dir, 'dashboard-template.html')
with open(template_path, 'r', encoding='utf-8') as f:
    t = f.read()

dados_json = json.dumps({'atualizado': '25/09/2026 10:55', 'leads': todos}, ensure_ascii=False)
with open(os.path.join(dash_dir, 'dashboard.html'), 'w', encoding='utf-8') as f:
    f.write(t.replace('__DADOS__', dados_json))

print("DONE")
