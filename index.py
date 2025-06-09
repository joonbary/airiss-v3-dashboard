from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from mangum import Mangum

app = FastAPI(title="AIRISS v3.0 - OK금융그룹 AI 인재분석시스템")

@app.get("/", response_class=HTMLResponse)
async def get_main_page():
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AIRISS v3.0 - OK금융그룹 AI 인재분석시스템</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Noto Sans KR', -apple-system, BlinkMacSystemFont, sans-serif;
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                min-height: 100vh;
                color: #333;
            }
            
            .header {
                background: rgba(255, 255, 255, 0.95);
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                padding: 1rem 0;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 2rem;
            }
            
            .header-content {
                display: flex;
                align-items: center;
                justify-content: space-between;
            }
            
            .logo {
                display: flex;
                align-items: center;
                gap: 1rem;
            }
            
            .logo-icon {
                width: 50px;
                height: 50px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 12px;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-weight: bold;
                font-size: 1.2rem;
            }
            
            .logo-text h1 {
                font-size: 1.5rem;
                color: #1e3c72;
                font-weight: 700;
            }
            
            .logo-text p {
                font-size: 0.9rem;
                color: #666;
            }
            
            .main-content {
                margin-top: 3rem;
                text-align: center;
                color: white;
            }
            
            .hero-section {
                padding: 4rem 0;
            }
            
            .hero-title {
                font-size: 3rem;
                font-weight: 700;
                margin-bottom: 1rem;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            }
            
            .hero-subtitle {
                font-size: 1.3rem;
                opacity: 0.9;
                margin-bottom: 3rem;
            }
            
            .features {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 2rem;
                margin-top: 3rem;
            }
            
            .feature-card {
                background: rgba(255, 255, 255, 0.9);
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            
            .feature-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
            }
            
            .feature-icon {
                font-size: 3rem;
                margin-bottom: 1rem;
            }
            
            .feature-title {
                font-size: 1.5rem;
                color: #1e3c72;
                margin-bottom: 0.5rem;
                font-weight: 600;
            }
            
            .feature-description {
                color: #666;
                line-height: 1.6;
            }
            
            .cta-section {
                margin-top: 4rem;
                padding: 2rem;
            }
            
            .cta-button {
                display: inline-block;
                padding: 1rem 3rem;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                text-decoration: none;
                border-radius: 50px;
                font-size: 1.1rem;
                font-weight: 600;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
            }
            
            .cta-button:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 30px rgba(102, 126, 234, 0.6);
            }
            
            .status-badge {
                display: inline-block;
                padding: 0.5rem 1rem;
                background: #4CAF50;
                color: white;
                border-radius: 20px;
                font-size: 0.9rem;
                font-weight: 500;
            }
            
            @media (max-width: 768px) {
                .hero-title {
                    font-size: 2rem;
                }
                
                .hero-subtitle {
                    font-size: 1.1rem;
                }
                
                .features {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    </head>
    <body>
        <header class="header">
            <div class="container">
                <div class="header-content">
                    <div class="logo">
                        <div class="logo-icon">AI</div>
                        <div class="logo-text">
                            <h1>AIRISS v3.0</h1>
                            <p>OK금융그룹 AI 인재분석시스템</p>
                        </div>
                    </div>
                    <div class="status-badge">
                        시스템 정상 작동중
                    </div>
                </div>
            </div>
        </header>
        
        <main class="main-content">
            <div class="container">
                <section class="hero-section">
                    <h2 class="hero-title">차세대 AI 인재분석 플랫폼</h2>
                    <p class="hero-subtitle">텍스트 분석과 정량 평가를 통합한 하이브리드 인재 분석 시스템</p>
                    
                    <div class="features">
                        <div class="feature-card">
                            <div class="feature-icon">📊</div>
                            <h3 class="feature-title">통합 대시보드</h3>
                            <p class="feature-description">
                                텍스트 분석과 정량 지표를 하나의 대시보드에서 확인하세요.
                                직관적인 시각화로 인재 현황을 한눈에 파악할 수 있습니다.
                            </p>
                        </div>
                        
                        <div class="feature-card">
                            <div class="feature-icon">🤖</div>
                            <h3 class="feature-title">AI 기반 분석</h3>
                            <p class="feature-description">
                                최신 AI 기술을 활용한 텍스트 분석으로 숨겨진 인사이트를 발견하세요.
                                개인별 맞춤형 피드백과 개선점을 제시합니다.
                            </p>
                        </div>
                        
                        <div class="feature-card">
                            <div class="feature-icon">📈</div>
                            <h3 class="feature-title">개인별 조회</h3>
                            <p class="feature-description">
                                레이더 차트와 상세 분석을 통해 개인별 역량을 다각도로 평가하세요.
                                강점과 개선점을 명확히 파악할 수 있습니다.
                            </p>
                        </div>
                    </div>
                    
                    <div class="cta-section">
                        <a href="/dashboard" class="cta-button">대시보드 시작하기</a>
                    </div>
                </section>
            </div>
        </main>
    </body>
    </html>
    """

@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "AIRISS v3.0",
        "message": "시스템이 정상적으로 작동중입니다"
    }

@app.get("/api/info")
async def get_info():
    return {
        "name": "AIRISS v3.0",
        "description": "OK금융그룹 AI 인재분석시스템",
        "version": "3.0.0",
        "features": [
            "텍스트 분석",
            "정량 평가",
            "개인별 대시보드",
            "AI 피드백"
        ]
    }

# Vercel serverless function handler
# Mangum is an adapter for running ASGI applications on AWS Lambda/Vercel
handler = Mangum(app)