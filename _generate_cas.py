#!/usr/bin/env python3
"""Generate FR/EN treatment case pages."""
import json
from pathlib import Path

ROOT = Path(__file__).parent

CASES = [
    {
        "slug_fr": "cou-epaules",
        "slug_en": "neck-shoulder-pain",
        "icon": "fa-user-injured",
        "title_fr": "Douleurs cervico-scapulaires",
        "title_en": "Neck and shoulder pain",
        "lead_fr": "Raideurs, tensions et douleurs au cou, aux épaules et entre les omoplates — une problématique fréquente liée au stress, à la posture ou au surmenage.",
        "lead_en": "Stiffness, tension and pain in the neck, shoulders and between the shoulder blades — often linked to stress, posture or overuse.",
        "symptoms_fr": [
            "Raideur au cou au réveil ou en fin de journée",
            "Douleur entre les omoplates ou vers la nuque",
            "Limitation des mouvements de rotation ou d'inclinaison",
            "Céphalées tensionnelles associées",
            "Engourdissements légers des bras (à évaluer médicalement si persistants)",
        ],
        "symptoms_en": [
            "Morning or end-of-day neck stiffness",
            "Pain between the shoulder blades or at the base of the neck",
            "Limited rotation or side bending",
            "Associated tension headaches",
            "Mild arm numbness (seek medical evaluation if persistent)",
        ],
        "approach_fr": "En médecine traditionnelle chinoise, les douleurs cervico-scapulaires sont souvent liées à la stagnation du Qi et du sang, aux tensions des méridiens du cou et des épaules, ou au stress accumulé. L'acupuncture vise à harmoniser la circulation, relâcher les tensions et soutenir l'équilibre global. La massothérapie (tissus profonds, points d'acupuncture, massage détente) complète le traitement en relâchant les muscles et améliorant la mobilité.",
        "approach_en": "In traditional Chinese medicine, neck and shoulder pain is often related to Qi and blood stagnation, tension along the neck and shoulder meridians, or accumulated stress. Acupuncture aims to harmonize circulation, release tension and support overall balance. Massage therapy (deep tissue, acupressure points, relaxation massage) complements care by easing muscles and improving mobility.",
        "services_fr": [
            ("Acupuncture classique", "../#services-acupuncture"),
            ("Massage des tissus profonds", "../#services-massage"),
            ("Massage des points d'acupuncture", "../#services-massage"),
            ("Thérapies intégrées (ventouses, gua sha)", "../#services-integrative"),
        ],
        "services_en": [
            ("Classic acupuncture", "../../en.html#services-acupuncture"),
            ("Deep tissue massage", "../../en.html#services-massage"),
            ("Acupressure massage", "../../en.html#services-massage"),
            ("Integrative therapies (cupping, gua sha)", "../../en.html#services-integrative"),
        ],
    },
    {
        "slug_fr": "mal-de-dos",
        "slug_en": "back-pain",
        "icon": "fa-bone",
        "title_fr": "Mal de dos",
        "title_en": "Back pain",
        "lead_fr": "Lombalgies, raideurs dorsales et inconforts persistants — l'acupuncture et la massothérapie peuvent accompagner votre récupération dans une approche personnalisée.",
        "lead_en": "Lower back pain, mid-back stiffness and persistent discomfort — acupuncture and massage therapy can support your recovery through personalized care.",
        "symptoms_fr": [
            "Douleur lombaire aiguë ou chronique",
            "Raideur en se levant ou après position assise prolongée",
            "Tension paravertébrale",
            "Difficulté à rester debout longtemps",
            "Douleur irradiant parfois vers la hanche (distincte de la sciatique)",
        ],
        "symptoms_en": [
            "Acute or chronic lower back pain",
            "Stiffness when standing up or after prolonged sitting",
            "Paravertebral muscle tension",
            "Difficulty standing for long periods",
            "Pain sometimes radiating to the hip (distinct from sciatica)",
        ],
        "approach_fr": "Le mal de dos est abordé en MTC selon la localisation, l'intensité et les facteurs aggravants (froid, fatigue, stress). L'acupuncture stimule les points et méridiens pour favoriser la circulation du Qi, soulager la douleur et soutenir la récupération. Le massage des tissus profonds, le massage suédois et les thérapies intégrées (ventouses, moxibustion) peuvent être intégrés au plan de soins.",
        "approach_en": "Back pain is addressed in TCM according to location, intensity and aggravating factors (cold, fatigue, stress). Acupuncture stimulates points and meridians to support Qi flow, ease pain and aid recovery. Deep tissue massage, Swedish massage and integrative therapies (cupping, moxibustion) may be included in the care plan.",
        "services_fr": [
            ("Acupuncture classique", "../#services-acupuncture"),
            ("Massage des tissus profonds", "../#services-massage"),
            ("Massage suédois", "../#services-massage"),
            ("Ventouses et moxibustion", "../#services-integrative"),
        ],
        "services_en": [
            ("Classic acupuncture", "../../en.html#services-acupuncture"),
            ("Deep tissue massage", "../../en.html#services-massage"),
            ("Swedish massage", "../../en.html#services-massage"),
            ("Cupping and moxibustion", "../../en.html#services-integrative"),
        ],
    },
    {
        "slug_fr": "sciatique",
        "slug_en": "sciatica",
        "icon": "fa-walking",
        "title_fr": "Sciatique",
        "title_en": "Sciatica",
        "lead_fr": "Douleur irradiant le long du nerf sciatique — une approche complémentaire peut aider à gérer l'inconfort et favoriser la détente musculaire.",
        "lead_en": "Pain radiating along the sciatic nerve — complementary care can help manage discomfort and promote muscular relaxation.",
        "symptoms_fr": [
            "Douleur partant du bas du dos ou de la fesse",
            "Irradiation le long de la cuisse, parfois jusqu'au pied",
            "Fourmillements ou engourdissements dans la jambe",
            "Aggravation à la marche, à la position assise ou en se penchant",
            "Raideur lombaire associée",
        ],
        "symptoms_en": [
            "Pain starting in the lower back or buttock",
            "Radiation along the thigh, sometimes to the foot",
            "Tingling or numbness in the leg",
            "Worse with walking, sitting or bending",
            "Associated lower back stiffness",
        ],
        "approach_fr": "La sciatique requiert une évaluation attentive. En MTC, on cherche à débloquer la stagnation le long des méridiens concernés, tonifier les zones déficientes et relâcher les tensions lombaires et pelviennes. L'acupuncture est souvent combinée à la massothérapie ciblée et, selon le cas, aux ventouses ou au gua sha. Nous accueillons aussi les dossiers SAAQ et CNESST lorsque le traitement est autorisé.",
        "approach_en": "Sciatica requires careful assessment. In TCM, care focuses on unblocking stagnation along affected meridians, tonifying deficient areas and releasing lumbar and pelvic tension. Acupuncture is often combined with targeted massage and, when appropriate, cupping or gua sha. We also welcome SAAQ and CNESST files when treatment is authorized.",
        "services_fr": [
            ("Acupuncture classique", "../#services-acupuncture"),
            ("Massage des tissus profonds", "../#services-massage"),
            ("Ventouses", "../#services-integrative"),
            ("Gua sha", "../#services-integrative"),
        ],
        "services_en": [
            ("Classic acupuncture", "../../en.html#services-acupuncture"),
            ("Deep tissue massage", "../../en.html#services-massage"),
            ("Cupping", "../../en.html#services-integrative"),
            ("Gua sha", "../../en.html#services-integrative"),
        ],
    },
    {
        "slug_fr": "insomnie",
        "slug_en": "insomnia",
        "icon": "fa-moon",
        "title_fr": "Insomnie",
        "title_en": "Insomnia",
        "lead_fr": "Difficulté à s'endormir, réveils nocturnes ou sommeil non réparateur — l'acupuncture et la massothérapie peuvent soutenir la détente et l'équilibre du système nerveux.",
        "lead_en": "Difficulty falling asleep, night waking or unrefreshing sleep — acupuncture and massage therapy can support relaxation and nervous system balance.",
        "symptoms_fr": [
            "Endormissement difficile ou prolongé",
            "Réveils fréquents en milieu de nuit",
            "Sommeil léger ou agité",
            "Fatigue au réveil malgré des heures au lit",
            "Irritabilité ou difficulté de concentration le jour",
        ],
        "symptoms_en": [
            "Prolonged difficulty falling asleep",
            "Frequent middle-of-the-night waking",
            "Light or restless sleep",
            "Fatigue on waking despite time in bed",
            "Daytime irritability or poor concentration",
        ],
        "approach_fr": "En MTC, l'insomnie est liée à un déséquilibre du Shen (esprit), du Yin et du Yang, ou à des tensions liées au stress. L'acupuncture harmonise les méridiens du cœur, du foie et des reins selon votre profil. Le massage détente, le massage du visage et les séances en fin de journée favorisent la relaxation. Un plan personnalisé peut inclure des conseils de rythme de vie adaptés à votre situation.",
        "approach_en": "In TCM, insomnia is linked to Shen (spirit) imbalance, Yin-Yang disharmony or stress-related tension. Acupuncture harmonizes the heart, liver and kidney meridians according to your profile. Relaxation massage, facial massage and late-day sessions promote calm. A personalized plan may include lifestyle rhythm guidance suited to your situation.",
        "services_fr": [
            ("Acupuncture classique", "../#services-acupuncture"),
            ("Massage détente", "../#services-massage"),
            ("Massage du visage", "../#services-massage"),
            ("Consultation + acupuncture (première visite)", "../#book"),
        ],
        "services_en": [
            ("Classic acupuncture", "../../en.html#services-acupuncture"),
            ("Relaxation massage", "../../en.html#services-massage"),
            ("Facial massage", "../../en.html#services-massage"),
            ("Consultation + acupuncture (first visit)", "../../en.html#book"),
        ],
    },
    {
        "slug_fr": "stress-anxiete",
        "slug_en": "stress-anxiety",
        "icon": "fa-spa",
        "title_fr": "Stress et anxiété",
        "title_en": "Stress and anxiety",
        "lead_fr": "Tension nerveuse, agitation, palpitations ou fatigue liée au stress — des soins holistiques pour retrouver calme et équilibre.",
        "lead_en": "Nervous tension, restlessness, palpitations or stress-related fatigue — holistic care to restore calm and balance.",
        "symptoms_fr": [
            "Tension musculaire généralisée",
            "Difficulté à se détendre ou à lâcher prise",
            "Sommeil perturbé",
            "Irritabilité, rumination ou sentiment d'oppression",
            "Fatigue malgré le repos",
        ],
        "symptoms_en": [
            "Generalized muscle tension",
            "Difficulty relaxing or unwinding",
            "Disrupted sleep",
            "Irritability, rumination or feeling of pressure",
            "Fatigue despite rest",
        ],
        "approach_fr": "Le stress et l'anxiété sont abordés en MTC par la régulation du Qi du foie, du cœur et de la rate, selon votre tableau clinique. L'acupuncture aide à apaiser le système nerveux et à rétablir l'harmonie intérieure. Le massage détente, le massage suédois et la réflexologie plantaire complètent efficacement les séances pour favoriser une détente profonde.",
        "approach_en": "Stress and anxiety are addressed in TCM by regulating liver, heart and spleen Qi according to your clinical pattern. Acupuncture helps calm the nervous system and restore inner harmony. Relaxation massage, Swedish massage and foot reflexology effectively complement sessions to encourage deep relaxation.",
        "services_fr": [
            ("Acupuncture classique", "../#services-acupuncture"),
            ("Massage détente", "../#services-massage"),
            ("Réflexologie plantaire", "../#services-massage"),
            ("Massage suédois", "../#services-massage"),
        ],
        "services_en": [
            ("Classic acupuncture", "../../en.html#services-acupuncture"),
            ("Relaxation massage", "../../en.html#services-massage"),
            ("Foot reflexology", "../../en.html#services-massage"),
            ("Swedish massage", "../../en.html#services-massage"),
        ],
    },
    {
        "slug_fr": "migraine",
        "slug_en": "migraine",
        "icon": "fa-head-side-virus",
        "title_fr": "Migraines",
        "title_en": "Migraines",
        "lead_fr": "Céphalées récurrentes, souvent pulsatile ou unilatérales — l'acupuncture peut accompagner la prévention et le soulagement des épisodes.",
        "lead_en": "Recurrent headaches, often pulsating or one-sided — acupuncture can support prevention and relief of episodes, as a complement to medical follow-up.",
        "symptoms_fr": [
            "Douleur pulsatile ou lancinante",
            "Sensibilité à la lumière ou au bruit",
            "Nausées parfois associées",
            "Douleur unilatérale ou localisée",
            "Aura visuelle chez certaines personnes",
        ],
        "symptoms_en": [
            "Pulsating or stabbing pain",
            "Sensitivity to light or sound",
            "Sometimes associated nausea",
            "One-sided or localized pain",
            "Visual aura in some individuals",
        ],
        "approach_fr": "Les migraines sont étudiées en MTC selon la zone touchée, les facteurs déclenchants et la constitution. L'acupuncture vise à harmoniser le Yang du foie, apaiser le Shen et réguler la circulation du Qi et du sang vers la tête. Des séances régulières peuvent contribuer à réduire la fréquence et l'intensité des crises, en complément du suivi médical.",
        "approach_en": "Migraines are assessed in TCM according to affected area, triggers and constitution. Acupuncture aims to harmonize liver Yang, calm the Shen and regulate Qi and blood flow to the head. Regular sessions may help reduce frequency and intensity of attacks, as a complement to medical follow-up.",
        "services_fr": [
            ("Acupuncture classique", "../#services-acupuncture"),
            ("Massage du visage et du cou", "../#services-massage"),
            ("Massage des points d'acupuncture", "../#services-massage"),
            ("Massage détente", "../#services-massage"),
        ],
        "services_en": [
            ("Classic acupuncture", "../../en.html#services-acupuncture"),
            ("Facial and neck massage", "../../en.html#services-massage"),
            ("Acupressure massage", "../../en.html#services-massage"),
            ("Relaxation massage", "../../en.html#services-massage"),
        ],
    },
]


def header_fr(base: str, active_cas: bool = False, lang_href: str = "../en/cases/", fr_href: str = "../cas/") -> str:
    cas_cls = ' class="nav-book"' if active_cas else ""
    return f"""    <header class="site-header" id="top">
        <div class="container header-inner">
            <nav class="navbar">
                <a href="{base}" class="logo" aria-label="Clinique Bien-Être Acupuncture et Massage">
                    <span class="logo-line"><span class="logo-clinique">Clinique</span><span class="logo-brand"> Bien-Être</span></span>
                    <span class="logo-line logo-line--sub">Acupuncture et Massage</span>
                </a>
                <button class="mobile-menu-btn" type="button" aria-label="Menu" aria-expanded="false" aria-controls="site-nav"><i class="fas fa-bars"></i></button>
                <ul class="nav-links" id="site-nav">
                    <li><a href="{base}">Accueil</a></li>
                    <li><a href="{base}#services">Services</a></li>
                    <li><a href="{base}#about">Philosophie</a></li>
                    <li><a href="{base}#book">Réserver</a></li>
                    <li><a href="{base}cas/"{cas_cls}>Cas cliniques</a></li>
                    <li><a href="{base}#faq">FAQ</a></li>
                    <li><a href="{base}#contact">Contact</a></li>
                    <li class="lang-switch">
                        <a href="{fr_href}" class="active" hreflang="fr" lang="fr">FR</a>
                        <span aria-hidden="true">|</span>
                        <a href="{lang_href}" hreflang="en" lang="en">EN</a>
                    </li>
                </ul>
                <a href="{base}#book" class="btn btn-sm nav-cta">Réserver</a>
            </nav>
        </div>
    </header>"""


def header_en(base: str, lang_href: str = "../../cas/", en_href: str = "../cases/") -> str:
    return f"""    <header class="site-header" id="top">
        <div class="container header-inner">
            <nav class="navbar">
                <a href="{base}en.html" class="logo" aria-label="Clinique Bien-Être Acupuncture et Massage">
                    <span class="logo-line"><span class="logo-clinique">Clinique</span><span class="logo-brand"> Bien-Être</span></span>
                    <span class="logo-line logo-line--sub">Acupuncture et Massage</span>
                </a>
                <button class="mobile-menu-btn" type="button" aria-label="Menu" aria-expanded="false" aria-controls="site-nav"><i class="fas fa-bars"></i></button>
                <ul class="nav-links" id="site-nav">
                    <li><a href="{base}en.html">Home</a></li>
                    <li><a href="{base}en.html#services">Services</a></li>
                    <li><a href="{base}en.html#about">Philosophy</a></li>
                    <li><a href="{base}en.html#book">Book</a></li>
                    <li><a href="{base}en/cases/" class="nav-book">Cases</a></li>
                    <li><a href="{base}en.html#faq">FAQ</a></li>
                    <li><a href="{base}en.html#contact">Contact</a></li>
                    <li class="lang-switch">
                        <a href="{lang_href}" hreflang="fr" lang="fr">FR</a>
                        <span aria-hidden="true">|</span>
                        <a href="{en_href}" class="active" hreflang="en" lang="en">EN</a>
                    </li>
                </ul>
                <a href="{base}en.html#book" class="btn btn-sm nav-cta">Book</a>
            </nav>
        </div>
    </header>"""


FOOTER_JS = """
    <script>
        (function () {
            const header = document.querySelector('.site-header');
            if (header) {
                const onScroll = () => header.classList.toggle('is-scrolled', window.scrollY > 24);
                window.addEventListener('scroll', onScroll, { passive: true });
                onScroll();
            }
            const btn = document.querySelector('.mobile-menu-btn');
            const nav = document.querySelector('.nav-links');
            if (btn && nav) {
                btn.addEventListener('click', () => {
                    const open = nav.classList.toggle('active');
                    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
                });
                nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
                    nav.classList.remove('active');
                    btn.setAttribute('aria-expanded', 'false');
                }));
            }
        })();
    </script>
</body>
</html>
"""


def case_json_ld(case: dict, lang: str) -> str:
    fr = lang == "fr"
    title = case["title_fr"] if fr else case["title_en"]
    lead = case["lead_fr"] if fr else case["lead_en"]
    slug = case["slug_fr"] if fr else case["slug_en"]
    base = "https://bienetreclinique.ca/cas" if fr else "https://bienetreclinique.ca/en/cases"
    url = f"{base}/{slug}.html"
    alt_url = f"https://bienetreclinique.ca/en/cases/{case['slug_en']}.html" if fr else f"https://bienetreclinique.ca/cas/{case['slug_fr']}.html"
    hub_name = "Cas cliniques" if fr else "Clinical cases"
    hub_url = "https://bienetreclinique.ca/cas/" if fr else "https://bienetreclinique.ca/en/cases/"
    home = "https://bienetreclinique.ca/" if fr else "https://bienetreclinique.ca/en.html"
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "MedicalWebPage",
                "@id": f"{url}#webpage",
                "url": url,
                "name": title,
                "description": lead,
                "inLanguage": "fr-CA" if fr else "en-CA",
                "isPartOf": {"@id": "https://bienetreclinique.ca/#website"},
                "about": {"@type": "MedicalCondition", "name": title},
                "publisher": {"@id": "https://bienetreclinique.ca/#clinic"},
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Accueil" if fr else "Home", "item": home},
                    {"@type": "ListItem", "position": 2, "name": hub_name, "item": hub_url},
                    {"@type": "ListItem", "position": 3, "name": title, "item": url},
                ],
            },
        ],
    }
    return f'    <script type="application/ld+json">\n{json.dumps(data, ensure_ascii=False, indent=2)}\n    </script>'


def hub_json_ld(lang: str) -> str:
    fr = lang == "fr"
    base = "https://bienetreclinique.ca/cas/" if fr else "https://bienetreclinique.ca/en/cases/"
    items = []
    for i, c in enumerate(CASES, 1):
        slug = c["slug_fr"] if fr else c["slug_en"]
        items.append({
            "@type": "ListItem",
            "position": i,
            "name": c["title_fr"] if fr else c["title_en"],
            "url": f"{base.rstrip('/')}/{slug}.html",
        })
    data = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Cas cliniques" if fr else "Clinical cases",
        "url": base,
        "itemListElement": items,
    }
    return f'    <script type="application/ld+json">\n{json.dumps(data, ensure_ascii=False, indent=2)}\n    </script>'


def render_case(case: dict, lang: str) -> str:
    fr = lang == "fr"
    if fr:
        css = "../css/"
        base = "../"
        hub = "../cas/"
        slug = case["slug_fr"]
        en_link = f"../en/cases/{case['slug_en']}.html"
        title = case["title_fr"]
        lead = case["lead_fr"]
        symptoms = case["symptoms_fr"]
        approach = case["approach_fr"]
        services = case["services_fr"]
        book = "../#book"
        home = "../"
        meta_desc = f"{title} — acupuncture et massothérapie à Brossard. Clinique Bien-Être, Rive-Sud."
        canonical = f"https://bienetreclinique.ca/cas/{slug}.html"
        alt_en = f'<link rel="alternate" hreflang="en-CA" href="https://bienetreclinique.ca/en/cases/{case["slug_en"]}.html">'
        lbl_sym = "Manifestations courantes"
        lbl_app = "Notre approche en MTC"
        lbl_svc = "Soins recommandés"
        lbl_cta = "Prendre rendez-vous"
        lbl_disc = "Les informations présentées sont à titre informatif et ne remplacent pas l'avis d'un professionnel de la santé. Les résultats varient selon chaque personne."
        breadcrumb = f'<a href="{home}">Accueil</a> · <a href="{hub}">Cas cliniques</a> · {title}'
        hdr = header_fr(base, True, f"../en/cases/{case['slug_en']}.html", f"{case['slug_fr']}.html")
        lang_attr = "fr"
    else:
        css = "../../css/"
        base = "../../"
        hub = "../cases/"
        slug = case["slug_en"]
        en_link = ""
        title = case["title_en"]
        lead = case["lead_en"]
        symptoms = case["symptoms_en"]
        approach = case["approach_en"]
        services = case["services_en"]
        book = "../../en.html#book"
        home = "../../en.html"
        meta_desc = f"{title} — acupuncture and massage therapy in Brossard. Clinique Bien-Être, South Shore."
        canonical = f"https://bienetreclinique.ca/en/cases/{slug}.html"
        alt_en = f'<link rel="alternate" hreflang="fr-CA" href="https://bienetreclinique.ca/cas/{case["slug_fr"]}.html">'
        lbl_sym = "Common signs"
        lbl_app = "Our TCM approach"
        lbl_svc = "Recommended care"
        lbl_cta = "Book an appointment"
        lbl_disc = "This information is for educational purposes only and does not replace advice from a healthcare professional. Results vary from person to person."
        breadcrumb = f'<a href="{home}">Home</a> · <a href="{hub}">Clinical cases</a> · {title}'
        hdr = header_en(base, f"../../cas/{case['slug_fr']}.html", f"{case['slug_en']}.html")
        lang_attr = "en"

    sym_li = "\n".join(f"                    <li>{s}</li>" for s in symptoms)
    svc_li = "\n".join(f'                    <li><a href="{u}">{n}</a></li>' for n, u in services)
    skip = "Aller au contenu principal" if fr else "Skip to main content"
    json_ld = case_json_ld(case, lang)
    fr_canonical = f"https://bienetreclinique.ca/cas/{case['slug_fr']}.html"
    en_canonical = f"https://bienetreclinique.ca/en/cases/{case['slug_en']}.html"

    return f"""<!DOCTYPE html>
<html lang="{lang_attr}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Clinique Bien-Être — Brossard</title>
    <meta name="description" content="{meta_desc}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{canonical}">
    <link rel="alternate" hreflang="fr-CA" href="{fr_canonical}">
    <link rel="alternate" hreflang="en-CA" href="{en_canonical}">
    <link rel="alternate" hreflang="x-default" href="{fr_canonical}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" media="print" onload="this.media='all'">
    <noscript><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"></noscript>
    <link rel="stylesheet" href="{css}site.css">
    <link rel="stylesheet" href="{css}cas.css">
{json_ld}
</head>
<body>
    <a class="skip-link" href="#main">{skip}</a>
{hdr}
    <section class="case-hero" id="main">
        <div class="container">
            <p class="breadcrumb">{breadcrumb}</p>
            <h1>{title}</h1>
            <p class="case-lead">{lead}</p>
        </div>
    </section>

    <section class="case-body">
        <div class="container case-grid">
            <div class="case-main">
                <h2>{lbl_sym}</h2>
                <ul>
{sym_li}
                </ul>
                <h2>{lbl_app}</h2>
                <p>{approach}</p>
                <p class="case-disclaimer">{lbl_disc}</p>
            </div>
            <aside class="case-sidebar">
                <h3>{lbl_svc}</h3>
                <ul class="case-services">
{svc_li}
                </ul>
                <a href="{book}" class="btn" style="width:100%;justify-content:center;">{lbl_cta}</a>
            </aside>
        </div>
    </section>

    <footer>
        <div class="container">
            <div class="copyright">
                <p>&copy; 2026 Clinique Bien-Être Acupuncture et Massage. {'Tous droits réservés.' if fr else 'All rights reserved.'}</p>
                <p><small>{'Soins complémentaires — résultats variables.' if fr else 'Complementary care — results vary.'}</small></p>
            </div>
        </div>
    </footer>
{FOOTER_JS}"""


def render_hub(lang: str) -> str:
    fr = lang == "fr"
    cards = []
    for c in CASES:
        if fr:
            href = f"{c['slug_fr']}.html"
            title = c["title_fr"]
            lead = c["lead_fr"]
            read = "En savoir plus"
        else:
            href = f"{c['slug_en']}.html"
            title = c["title_en"]
            lead = c["lead_en"]
            read = "Learn more"
        cards.append(f"""            <a href="{href}" class="cas-hub-card">
                <i class="fas {c['icon']}"></i>
                <h2>{title}</h2>
                <p>{lead}</p>
                <span class="cas-link">{read} →</span>
            </a>""")
    grid = "\n".join(cards)

    if fr:
        css = "../css/"
        hdr = header_fr("../", True)
        title = "Cas cliniques"
        lead = "Découvrez comment l'acupuncture et la massothérapie peuvent accompagner différentes problématiques de santé, dans une approche personnalisée de la médecine traditionnelle chinoise."
        eyebrow = "Accompagnement thérapeutique"
        canonical = "https://bienetreclinique.ca/cas/"
        alt_en = "https://bienetreclinique.ca/en/cases/"
        lang_attr = "fr"
        skip = "Aller au contenu principal"
    else:
        css = "../../css/"
        hdr = header_en("../../")
        title = "Clinical cases"
        lead = "Learn how acupuncture and massage therapy can support various health concerns through personalized traditional Chinese medicine care."
        eyebrow = "Therapeutic support"
        canonical = "https://bienetreclinique.ca/en/cases/"
        alt_en = "https://bienetreclinique.ca/cas/"
        lang_attr = "en"
        skip = "Skip to main content"

    json_ld = hub_json_ld(lang)

    return f"""<!DOCTYPE html>
<html lang="{lang_attr}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Clinique Bien-Être — Brossard</title>
    <meta name="description" content="{lead}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{canonical}">
    <link rel="alternate" hreflang="fr-CA" href="https://bienetreclinique.ca/cas/">
    <link rel="alternate" hreflang="en-CA" href="https://bienetreclinique.ca/en/cases/">
    <link rel="alternate" hreflang="x-default" href="https://bienetreclinique.ca/cas/">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" media="print" onload="this.media='all'">
    <noscript><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"></noscript>
    <link rel="stylesheet" href="{css}site.css">
    <link rel="stylesheet" href="{css}cas.css">
{json_ld}
</head>
<body>
    <a class="skip-link" href="#main">{skip}</a>
{hdr}
    <section class="case-hero" id="main">
        <div class="container">
            <h1>{title}</h1>
            <p class="case-lead">{lead}</p>
        </div>
    </section>
    <section class="case-body" style="padding-top:48px;">
        <div class="container">
            <p class="section-head" style="text-align:center;margin-bottom:32px;"><span class="eyebrow">{eyebrow}</span></p>
            <div class="cas-hub-grid">
{grid}
            </div>
        </div>
    </section>
    <footer>
        <div class="container"><div class="copyright"><p>&copy; 2026 Clinique Bien-Être Acupuncture et Massage.</p></div></div>
    </footer>
{FOOTER_JS}"""


def main():
    (ROOT / "cas").mkdir(exist_ok=True)
    (ROOT / "en" / "cases").mkdir(parents=True, exist_ok=True)
    (ROOT / "cas" / "index.html").write_text(render_hub("fr"), encoding="utf-8")
    (ROOT / "en" / "cases" / "index.html").write_text(render_hub("en"), encoding="utf-8")
    for c in CASES:
        (ROOT / "cas" / f"{c['slug_fr']}.html").write_text(render_case(c, "fr"), encoding="utf-8")
        (ROOT / "en" / "cases" / f"{c['slug_en']}.html").write_text(render_case(c, "en"), encoding="utf-8")
    print("Generated", len(CASES) * 2 + 2, "pages")


if __name__ == "__main__":
    main()
