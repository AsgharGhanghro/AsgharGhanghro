<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ali Asghar | MERN Stack Developer</title>
    <style>
        :root {
            --primary: #6C63FF;
            --secondary: #4D44DB;
            --dark: #0F2027;
            --darker: #0A161A;
            --light: #F8F9FA;
            --gray: #6C757D;
            --success: #28A745;
            --danger: #DC3545;
            --warning: #FFC107;
            --info: #17A2B8;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
        }
        
        .container {
            background: white;
            border-radius: 12px;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            margin-bottom: 30px;
        }
        
        .header {
            text-align: center;
            padding: 40px 20px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            position: relative;
        }
        
        .profile-img {
            width: 180px;
            height: 180px;
            border-radius: 50%;
            object-fit: cover;
            border: 5px solid white;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }
        
        h1 {
            margin: 0;
            font-size: 2.5rem;
            font-weight: 700;
        }
        
        h2 {
            margin: 10px 0 0;
            font-size: 1.5rem;
            font-weight: 400;
            opacity: 0.9;
        }
        
        h3 {
            color: var(--primary);
            font-size: 1.8rem;
            margin-top: 40px;
            margin-bottom: 20px;
            position: relative;
            padding-bottom: 10px;
        }
        
        h3::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 60px;
            height: 3px;
            background: var(--primary);
        }
        
        .section {
            padding: 30px;
        }
        
        .about-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }
        
        .about-card {
            background: white;
            border-radius: 10px;
            padding: 25px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
            border-left: 4px solid var(--primary);
        }
        
        .tech-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 15px;
        }
        
        .tech-category {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
        }
        
        .tech-category h4 {
            margin-top: 0;
            color: var(--primary);
            font-size: 1.2rem;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
        }
        
        .badge {
            display: inline-block;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 0.85rem;
            margin: 5px;
            background: #f0f0f0;
            color: #333;
        }
        
        .badge-react { background: #61DAFB; color: black; }
        .badge-next { background: #000000; color: white; }
        .badge-tailwind { background: #38B2AC; color: white; }
        .badge-typescript { background: #3178C6; color: white; }
        .badge-node { background: #339933; color: white; }
        .badge-express { background: #000000; color: white; }
        .badge-python { background: #3776AB; color: white; }
        .badge-django { background: #092E20; color: white; }
        .badge-mongo { background: #47A248; color: white; }
        .badge-postgres { background: #4169E1; color: white; }
        .badge-mysql { background: #4479A1; color: white; }
        .badge-docker { background: #2496ED; color: white; }
        .badge-aws { background: #232F3E; color: white; }
        .badge-git { background: #F05032; color: white; }
        .badge-github { background: #2088FF; color: white; }
        
        .stats-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        
        .stat-card {
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
            text-align: center;
        }
        
        .social-links {
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
            margin-top: 30px;
        }
        
        .social-link {
            display: inline-block;
            padding: 10px 20px;
            border-radius: 30px;
            color: white;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .social-link:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }
        
        .link-linkedin { background: #0077B5; }
        .link-twitter { background: #1DA1F2; }
        .link-leetcode { background: #FFA116; color: black; }
        .link-gmail { background: #D14836; }
        .link-portfolio { background: var(--primary); }
        
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
        }
        
        .project-card {
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }
        
        .project-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        }
        
        .project-img {
            width: 100%;
            height: 180px;
            object-fit: cover;
        }
        
        .project-content {
            padding: 20px;
        }
        
        .project-title {
            margin: 0 0 10px;
            font-size: 1.3rem;
            color: var(--dark);
        }
        
        .project-desc {
            color: var(--gray);
            margin-bottom: 15px;
        }
        
        .project-link {
            display: inline-block;
            padding: 8px 15px;
            background: var(--primary);
            color: white;
            border-radius: 5px;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        
        .project-link:hover {
            background: var(--secondary);
        }
        
        .footer {
            text-align: center;
            padding: 20px;
            color: var(--gray);
            font-size: 0.9rem;
        }
        
        @media (max-width: 768px) {
            .about-grid, .tech-grid, .stats-container, .projects-grid {
                grid-template-columns: 1fr;
            }
            
            h1 {
                font-size: 2rem;
            }
            
            h2 {
                font-size: 1.2rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80" alt="Ali Asghar" class="profile-img">
            <h1>Ali Asghar</h1>
            <h2>MERN Stack Developer | Open Source Contributor | Tech Enthusiast</h2>
        </div>
        
        <div class="section">
            <h3>🚀 About Me</h3>
            <div class="about-grid">
                <div class="about-card">
                    <h4>Professional</h4>
                    <p>Passionate MERN stack developer with expertise in building scalable web applications. Currently focused on mastering modern web technologies and contributing to open source projects.</p>
                </div>
                <div class="about-card">
                    <h4>Skills</h4>
                    <p>Full-stack development with JavaScript/TypeScript, Python, and Java. Experience with cloud platforms (AWS), containerization (Docker), and CI/CD pipelines.</p>
                </div>
                <div class="about-card">
                    <h4>Interests</h4>
                    <p>Exploring new technologies, solving complex problems, and mentoring aspiring developers. Avid learner currently diving into Angular and Django ecosystems.</p>
                </div>
            </div>
        </div>
        
        <div class="section">
            <h3>🔧 Technologies & Tools</h3>
            <div class="tech-grid">
                <div class="tech-category">
                    <h4>Frontend</h4>
                    <span class="badge badge-react">React</span>
                    <span class="badge badge-next">Next.js</span>
                    <span class="badge badge-tailwind">Tailwind CSS</span>
                    <span class="badge badge-typescript">TypeScript</span>
                </div>
                <div class="tech-category">
                    <h4>Backend</h4>
                    <span class="badge badge-node">Node.js</span>
                    <span class="badge badge-express">Express</span>
                    <span class="badge badge-python">Python</span>
                    <span class="badge badge-django">Django</span>
                </div>
                <div class="tech-category">
                    <h4>Databases</h4>
                    <span class="badge badge-mongo">MongoDB</span>
                    <span class="badge badge-postgres">PostgreSQL</span>
                    <span class="badge badge-mysql">MySQL</span>
                </div>
                <div class="tech-category">
                    <h4>DevOps</h4>
                    <span class="badge badge-docker">Docker</span>
                    <span class="badge badge-aws">AWS</span>
                    <span class="badge badge-git">Git</span>
                    <span class="badge badge-github">GitHub Actions</span>
                </div>
            </div>
        </div>
        
        <div class="section">
            <h3>📈 GitHub Stats</h3>
            <div class="stats-container">
                <div class="stat-card">
                    <img src="https://github-readme-stats.vercel.app/api?username=aliasghar&show_icons=true&theme=radical&include_all_commits=true&count_private=true&bg_color=30,0F2027,203A43,2C5364&title_color=fff&text_color=fff&icon_color=6C63FF" alt="GitHub Stats" style="width: 100%;">
                </div>
                <div class="stat-card">
                    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=aliasghar&layout=compact&langs_count=8&theme=radical&bg_color=30,0F2027,203A43,2C5364&title_color=fff&text_color=fff" alt="Top Languages" style="width: 100%;">
                </div>
            </div>
            <div class="stat-card" style="margin-top: 20px;">
                <img src="https://github-readme-streak-stats.herokuapp.com/?user=aliasghar&theme=radical&background=0F2027&stroke=6C63FF&ring=6C63FF&fire=6C63FF&currStreakNum=fff&currStreakLabel=6C63FF" alt="GitHub Streak" style="width: 100%;">
            </div>
        </div>
        
        <div class="section">
            <h3>🔥 Recent Projects</h3>
            <div class="projects-grid">
                <div class="project-card">
                    <img src="https://images.unsplash.com/photo-1508672019048-805c876b67e2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=600&q=80" alt="Travel Agency" class="project-img">
                    <div class="project-content">
                        <h4 class="project-title">Traveling Agency</h4>
                        <p class="project-desc">A modern travel booking platform built with Next.js and MongoDB</p>
                        <a href="https://traveling-agency-ke8z.vercel.app/" class="project-link" target="_blank">View Project</a>
                    </div>
                </div>
                <div class="project-card">
                    <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=600&q=80" alt="E-Commerce Dashboard" class="project-img">
                    <div class="project-content">
                        <h4 class="project-title">E-Commerce Dashboard</h4>
                        <p class="project-desc">Admin dashboard for e-commerce stores with React and Node.js</p>
                        <a href="https://github.com/aliasghar/ecommerce-dashboard" class="project-link" target="_blank">View Project</a>
                    </div>
                </div>
                <div class="project-card">
                    <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=600&q=80" alt="Blog CMS" class="project-img">
                    <div class="project-content">
                        <h4 class="project-title">Blog CMS</h4>
                        <p class="project-desc">Content management system for bloggers using Django and PostgreSQL</p>
                        <a href="https://github.com/aliasghar/blog-cms" class="project-link" target="_blank">View Project</a>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="section">
            <h3>🌐 Connect With Me</h3>
            <div class="social-links">
                <a href="https://linkedin.com/in/ali-asghar-a730322bb" class="social-link link-linkedin" target="_blank">LinkedIn</a>
                <a href="https://twitter.com/aliasghar" class="social-link link-twitter" target="_blank">Twitter</a>
                <a href="https://leetcode.com/ali-asghar-102938475" class="social-link link-leetcode" target="_blank">LeetCode</a>
                <a href="mailto:aliasghargh540@gmail.com" class="social-link link-gmail" target="_blank">Gmail</a>
                <a href="#" class="social-link link-portfolio" target="_blank">Portfolio</a>
            </div>
        </div>
        
        <div class="footer">
            <p>© 2023 Ali Asghar | Made with ❤️ for the developer community</p>
            <p>
                <img src="https://komarev.com/ghpvc/?username=aliasghar&label=Profile%20views&color=6C63FF&style=flat" alt="profile views"> 
                <img src="https://visitor-badge.laobi.icu/badge?page_id=aliasghar.aliasghar" alt="visitors">
            </p>
        </div>
    </div>
</body>
</html>
