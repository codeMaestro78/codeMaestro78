<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Devarshi Lalani - Portfolio</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            overflow-x: hidden;
            line-height: 1.6;
        }

        /* Animated Background */
        .bg-animation {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            opacity: 0.1;
        }

        .bg-animation::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="20" cy="20" r="2" fill="white"><animate attributeName="opacity" values="0;1;0" dur="3s" repeatCount="indefinite"/></circle><circle cx="80" cy="30" r="1.5" fill="white"><animate attributeName="opacity" values="0;1;0" dur="4s" repeatCount="indefinite" begin="1s"/></circle><circle cx="50" cy="70" r="1" fill="white"><animate attributeName="opacity" values="0;1;0" dur="2s" repeatCount="indefinite" begin="2s"/></circle></svg>') repeat;
            animation: float 20s linear infinite;
        }

        @keyframes float {
            0% { transform: translateY(0); }
            100% { transform: translateY(-100px); }
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            position: relative;
            z-index: 1;
        }

        /* Header Section */
        .header {
            text-align: center;
            padding: 60px 0;
            position: relative;
        }

        .profile-avatar {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            margin: 0 auto 30px;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4);
            background-size: 400% 400%;
            animation: gradientShift 4s ease infinite, pulse 2s ease-in-out infinite alternate;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 80px;
            font-weight: bold;
            color: white;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            position: relative;
            overflow: hidden;
        }

        .profile-avatar::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(255,255,255,0.3), transparent);
            transform: rotate(45deg);
            animation: shine 3s linear infinite;
        }

        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            100% { transform: scale(1.05); }
        }

        @keyframes shine {
            0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
            100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
        }

        .name {
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 10px;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: textGlow 2s ease-in-out infinite alternate;
        }

        @keyframes textGlow {
            0% { text-shadow: 0 0 20px rgba(255, 107, 107, 0.5); }
            100% { text-shadow: 0 0 30px rgba(78, 205, 196, 0.8); }
        }

        .role {
            font-size: 1.5rem;
            opacity: 0.9;
            margin-bottom: 30px;
            animation: slideInUp 1s ease-out 0.5s both;
        }

        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 0.9;
                transform: translateY(0);
            }
        }

        /* Skills Section */
        .section {
            margin: 60px 0;
            padding: 40px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            animation: fadeInUp 1s ease-out;
            position: relative;
            overflow: hidden;
        }

        .section::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            animation: shimmer 3s linear infinite;
        }

        @keyframes shimmer {
            0% { left: -100%; }
            100% { left: 100%; }
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(40px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .section-title {
            font-size: 2.5rem;
            margin-bottom: 30px;
            text-align: center;
            position: relative;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 100px;
            height: 3px;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            border-radius: 2px;
        }

        /* Skills Grid */
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }

        .skill-category {
            background: rgba(255, 255, 255, 0.1);
            padding: 25px;
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }

        .skill-category::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(45deg, rgba(255,107,107,0.1), rgba(78,205,196,0.1));
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .skill-category:hover::before {
            opacity: 1;
        }

        .skill-category:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }

        .skill-category h3 {
            font-size: 1.3rem;
            margin-bottom: 15px;
            color: #4ecdc4;
        }

        .skill-tag {
            display: inline-block;
            background: rgba(255, 255, 255, 0.2);
            padding: 5px 12px;
            margin: 3px;
            border-radius: 20px;
            font-size: 0.9rem;
            transition: all 0.3s ease;
            border: 1px solid rgba(255, 255, 255, 0.3);
        }

        .skill-tag:hover {
            background: rgba(255, 107, 107, 0.3);
            transform: scale(1.05);
        }

        /* Tech Stack Icons */
        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin: 40px 0;
        }

        .tech-icon {
            width: 80px;
            height: 80px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            transition: all 0.3s ease;
            border: 2px solid rgba(255, 255, 255, 0.2);
            position: relative;
            overflow: hidden;
        }

        .tech-icon::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .tech-icon:hover::before {
            opacity: 0.2;
        }

        .tech-icon:hover {
            transform: rotateY(180deg) scale(1.1);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
        }

        /* Projects Section */
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            margin-top: 30px;
        }

        .project-card {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 30px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            cursor: pointer;
        }

        .project-card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: conic-gradient(from 0deg, transparent, rgba(255,107,107,0.1), transparent, rgba(78,205,196,0.1), transparent);
            animation: rotate 4s linear infinite;
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .project-card:hover::before {
            opacity: 1;
        }

        @keyframes rotate {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .project-card:hover {
            transform: translateY(-15px);
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
        }

        .project-emoji {
            font-size: 2.5rem;
            margin-bottom: 15px;
            display: block;
            animation: bounce 2s ease-in-out infinite;
        }

        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-10px); }
            60% { transform: translateY(-5px); }
        }

        .project-title {
            font-size: 1.5rem;
            margin-bottom: 15px;
            color: #4ecdc4;
        }

        .project-description {
            opacity: 0.9;
            line-height: 1.6;
        }

        /* Stats Section */
        .stats-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            margin: 40px 0;
        }

        .stat-card {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4);
            background-size: 400% 400%;
            animation: gradientShift 3s ease infinite;
        }

        .stat-card:hover {
            transform: scale(1.05);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }

        .stat-number {
            font-size: 3rem;
            font-weight: bold;
            color: #4ecdc4;
            margin-bottom: 10px;
            animation: countUp 2s ease-out;
        }

        @keyframes countUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .stat-label {
            font-size: 1.1rem;
            opacity: 0.9;
        }

        /* Contact Section */
        .contact-links {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin: 40px 0;
            flex-wrap: wrap;
        }

        .contact-link {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 15px 25px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50px;
            text-decoration: none;
            color: white;
            transition: all 0.3s ease;
            border: 2px solid rgba(255, 255, 255, 0.2);
            position: relative;
            overflow: hidden;
        }

        .contact-link::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: left 0.5s ease;
        }

        .contact-link:hover::before {
            left: 100%;
        }

        .contact-link:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
            background: rgba(255, 107, 107, 0.2);
        }

        /* Fun Fact Section */
        .fun-fact {
            text-align: center;
            padding: 40px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            margin: 40px 0;
            border: 1px solid rgba(255, 255, 255, 0.1);
            position: relative;
        }

        .fun-fact::before {
            content: '💡';
            position: absolute;
            top: -20px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 2rem;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            width: 60px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
            animation: bounce 2s ease-in-out infinite;
        }

        .quote {
            font-size: 1.3rem;
            font-style: italic;
            margin-top: 20px;
            opacity: 0.9;
            animation: typewriter 4s steps(100) 1s both;
        }

        @keyframes typewriter {
            from { width: 0; }
            to { width: 100%; }
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .name { font-size: 2.5rem; }
            .section-title { font-size: 2rem; }
            .profile-avatar { width: 150px; height: 150px; font-size: 60px; }
            .projects-grid { grid-template-columns: 1fr; }
            .contact-links { flex-direction: column; align-items: center; }
            .tech-stack { gap: 15px; }
            .tech-icon { width: 60px; height: 60px; font-size: 1.5rem; }
        }

        /* Scroll Animation */
        .scroll-indicator {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: rgba(255, 255, 255, 0.1);
            z-index: 1000;
        }

        .scroll-progress {
            height: 100%;
            background: linear-gradient(90deg, #ff6b6b, #4ecdc4);
            width: 0%;
            transition: width 0.1s ease;
        }

        /* Floating Action Button */
        .fab {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 60px;
            height: 60px;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.5rem;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
            z-index: 1000;
            animation: pulse 2s ease-in-out infinite alternate;
        }

        .fab:hover {
            transform: scale(1.1);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4);
        }

        /* Theme Toggle */
        .theme-toggle {
            position: fixed;
            top: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            z-index: 1000;
        }

        .theme-toggle:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: rotate(180deg);
        }
    </style>
</head>
<body>
    <div class="bg-animation"></div>
    
    <div class="scroll-indicator">
        <div class="scroll-progress" id="scrollProgress"></div>
    </div>

    <div class="theme-toggle" onclick="toggleTheme()" title="Toggle Theme">
        🌓
    </div>

    <div class="fab" onclick="scrollToTop()" title="Back to Top">
        ↑
    </div>

    <div class="container">
        <!-- Header Section -->
        <div class="header">
            <div class="profile-avatar">DL</div>
            <h1 class="name">Devarshi Lalani</h1>
            <p class="role">Software Developer | Web 3.0 Enthusiast</p>
            <div style="font-size: 1.2rem; opacity: 0.8;">🎓 LJ University</div>
        </div>

        <!-- Skills Section -->
        <div class="section">
            <h2 class="section-title">🚀 Technologies & Skills</h2>
            
            <div class="tech-stack">
                <div class="tech-icon" title="Java">☕</div>
                <div class="tech-icon" title="C++">⚡</div>
                <div class="tech-icon" title="Python">🐍</div>
                <div class="tech-icon" title="JavaScript">📜</div>
                <div class="tech-icon" title="React">⚛️</div>
                <div class="tech-icon" title="Node.js">📗</div>
                <div class="tech-icon" title="MongoDB">🍃</div>
                <div class="tech-icon" title="Git">🌿</div>
                <div class="tech-icon" title="Docker">🐳</div>
                <div class="tech-icon" title="AWS">☁️</div>
                <div class="tech-icon" title="Blockchain">⛓️</div>
                <div class="tech-icon" title="AI/ML">🤖</div>
            </div>

            <div class="skills-grid">
                <div class="skill-category">
                    <h3>Frontend Development</h3>
                    <div class="skill-tag">React</div>
                    <div class="skill-tag">JavaScript</div>
                    <div class="skill-tag">HTML5</div>
                    <div class="skill-tag">CSS3</div>
                    <div class="skill-tag">Tailwind CSS</div>
                </div>
                <div class="skill-category">
                    <h3>Backend Development</h3>
                    <div class="skill-tag">Node.js</div>
                    <div class="skill-tag">Express.js</div>
                    <div class="skill-tag">MongoDB</div>
                    <div class="skill-tag">Python</div>
                    <div class="skill-tag">Django</div>
                </div>
                <div class="skill-category">
                    <h3>Programming Languages</h3>
                    <div class="skill-tag">Java</div>
                    <div class="skill-tag">C++</div>
                    <div class="skill-tag">Python</div>
                    <div class="skill-tag">JavaScript</div>
                    <div class="skill-tag">Solidity</div>
                </div>
                <div class="skill-category">
                    <h3>Emerging Technologies</h3>
                    <div class="skill-tag">Blockchain</div>
                    <div class="skill-tag">Web 3.0</div>
                    <div class="skill-tag">AI/ML</div>
                    <div class="skill-tag">Smart Contracts</div>
                    <div class="skill-tag">DApps</div>
                </div>
            </div>
        </div>

        <!-- Stats Section -->
        <div class="section">
            <h2 class="section-title">📊 GitHub Statistics</h2>
            <div class="stats-container">
                <div class="stat-card">
                    <div class="stat-number">150+</div>
                    <div class="stat-label">Repositories</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">500+</div>
                    <div class="stat-label">Commits</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">25+</div>
                    <div class="stat-label">Projects</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">15+</div>
                    <div class="stat-label">Languages</div>
                </div>
            </div>
        </div>

        <!-- Projects Section -->
        <div class="section">
            <h2 class="section-title">🏆 Featured Projects</h2>
            <div class="projects-grid">
                <div class="project-card">
                    <span class="project-emoji">🚑</span>
                    <h3 class="project-title">Hospital Management System</h3>
                    <p class="project-description">Java 8.0-based comprehensive system handling hospital operations, including patient management, appointment scheduling, and staff coordination with modern GUI interface.</p>
                </div>
                <div class="project-card">
                    <span class="project-emoji">📈</span>
                    <h3 class="project-title">StockMatrix</h3>
                    <p class="project-description">Advanced platform focused on technical and fundamental stock market analysis, helping investors make data-driven decisions with real-time market insights and AI predictions.</p>
                </div>
                <div class="project-card">
                    <span class="project-emoji">💰</span>
                    <h3 class="project-title">Cryptocurrency Portfolio Tracker</h3>
                    <p class="project-description">Java & XAMPP-based application enabling users to track and manage cryptocurrency investments with real-time market data and portfolio analytics.</p>
                </div>
                <div class="project-card">
                    <span class="project-emoji">🛍️</span>
                    <h3 class="project-title">TrendHive</h3>
                    <p class="project-description">Fashion e-commerce platform using AI-powered personalized recommendations for enhanced shopping experience with machine learning algorithms.</p>
                </div>
                <div class="project-card">
                    <span class="project-emoji">📡</span>
                    <h3 class="project-title">P2P File Sharing System</h3>
                    <p class="project-description">Secure and efficient decentralized file-sharing system using advanced cryptography and UDP/TCP protocols for seamless peer-to-peer communication.</p>
                </div>
                <div class="project-card">
                    <span class="project-emoji">🔗</span>
                    <h3 class="project-title">Smart Contract DApp</h3>
                    <p class="project-description">Decentralized application built on Ethereum blockchain with Solidity smart contracts, featuring Web3 integration and modern React frontend.</p>
                </div>
            </div>
        </div>

        <!-- Currently Learning Section -->
        <div class="section">
            <h2 class="section-title">🌱 Currently Exploring</h2>
            <div class="skills-grid">
                <div class="skill-category">
                    <h3>🔗 Web 3.0 Development</h3>
                    <div class="skill-tag">Blockchain</div>
                    <div class="skill-tag">Smart Contracts</div>
                    <div class="skill-tag">DApps</div>
                    <div class="skill-tag">Ethereum</div>
                </div>
                <div class="skill-category">
                    <h3>⚛️ Advanced React</h3>
                    <div class="skill-tag">React Patterns</div>
                    <div class="skill-tag">Performance Optimization</div>
                    <div class="skill-tag">Next.js</div>
                    <div class="skill-tag">Redux Toolkit</div>
                </div>
                <div class="skill-category">
                    <h3>🏗️ Backend Architecture</h3>
                    <div class="skill-tag">Microservices</div>
                    <div class="skill-tag">Scalable Systems</div>
                    <div class="skill-tag">API Design</div>
                    <div class="skill-tag">Database Optimization</div>
                </div>
                <div class="skill-category">
                    <h3>🤖 AI & Machine Learning</h3>
                    <div class="skill-tag">Deep Learning</div>
                    <div class="skill-tag">NLP</div>
                    <div class="skill-tag">TensorFlow</div>
                    <div class="skill-tag">PyTorch</div>
                </div>
                <div class="skill-category">
                    <h3>☁️ Cloud & DevOps</h3>
                    <div class="skill-tag">AWS</div>
                    <div class="skill-tag">Docker</div>
                    <div class="skill-tag">Kubernetes</div>
                    <div class="skill-tag">CI/CD</div>
                </div>
                <div class="skill-category">
                    <h3>📊 Financial Technology</h3>
                    <div class="skill-tag">Algorithmic Trading</div>
                    <div class="skill-tag">Financial Analysis</div>
                    <div class="skill-tag">Quantitative Models</div>
                    <div class="skill-tag">Market Data APIs</div>
                </div>
            </div>
        </div>

        <!-- Contact Section -->
        <div class="section">
            <h2 class="section-title">📫 Let's Connect</h2>
            <div class="contact-links">
                <a href="https://linkedin.com/in/devarshilalani05" class="contact-link" target="_blank">
                    <span>💼</span>
                    <span>LinkedIn</span>
                </a>
                <a href="https://github.com/codeMaestro78" class="contact-link" target="_blank">
                    <span>🐙</span>
                    <span>GitHub</span>
                </a>
                <a href="mailto:thelogical369@gmail.com" class="contact-link">
                    <span>📧</span>
                    <span>Email</span>
                </a>
                <a href="https://twitter.com/DevarshiLalani" class="contact-link" target="_blank">
                    <span>🐦</span>
                    <span>Twitter</span>
