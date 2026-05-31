import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# FIX 2: Chrome dots colors
# Search for .m-chrome-circle { ... } and add :nth-child rules after it
html = re.sub(
    r'(\.m-chrome-circle\s*\{[^}]*\})',
    r'\1\n    .m-chrome-circle:nth-child(1) { background-color: #FF5F57; }\n    .m-chrome-circle:nth-child(2) { background-color: #FEBC2E; }\n    .m-chrome-circle:nth-child(3) { background-color: #28C840; }',
    html
)

# FIX 4: Spacing
# Add margin-top: 40px to .dash-caption
html = re.sub(
    r'(/\*\s*STORY PANELS \/ ROADMAP\s*\*/)',
    r'\1\n    .dash-caption {\n      margin-top: 40px;\n    }',
    html
)
# Add margin-top: 80px to .roadmap-panel
html = re.sub(
    r'(\.roadmap-panel\s*\{[^}]*padding:\s*56px;)',
    r'\1\n      margin-top: 80px;',
    html
)

# FIX 5: Mobile responsiveness
mobile_css = """@media (max-width: 767px) {
      /* General Typography floor handled below by global regex */
      
      /* Tap targets */
      a, button, .cta-button, .text-cta {
        min-height: 44px;
      }
      
      .pill-nav {
        padding: 12px 12px;
        width: calc(100% - 24px);
      }
      .nav-tag {
        display: none;
      }
      .wordmark {
        font-size: 13px;
      }
      .cta-button {
        padding: 8px 14px;
      }
      
      .section-1 {
        padding: 70px 24px;
      }
      .hero-headline {
        font-size: 2rem;
      }
      .hero-subline {
        font-size: 15px;
      }
      
      .section-2 {
        padding: 70px 24px 84px 24px;
      }
      
      .offers-row {
        grid-template-columns: 1fr;
        display: flex;
        flex-direction: column;
      }
      .offers-grid {
        display: flex;
        flex-direction: column;
      }
      .offer-block {
        width: 100%;
        padding: 28px;
        box-sizing: border-box;
      }
      .deliverables.two-col {
        grid-template-columns: 1fr;
      }
      
      .module-panel {
        padding: 28px;
      }
      .module-content {
        grid-template-columns: 1fr;
        gap: 24px;
        display: flex;
        flex-direction: column;
      }
      .module-prose {
        max-width: none;
      }
      .module-deliverables {
        grid-template-columns: 1fr;
      }
      
      .dashboard-wrapper {
        overflow-x: auto;
        scrollbar-width: none;
        -ms-overflow-style: none;
        perspective: none;
      }
      .dashboard-wrapper::-webkit-scrollbar {
        display: none;
      }
      .dashboard-mockup {
        transform: none !important;
        border-radius: 4px;
        min-width: 600px;
      }
      .dashboard-mockup.reveal {
        transform: translateY(28px) !important;
      }
      .dashboard-mockup.reveal.active {
        transform: translateY(0) !important;
      }
      .dashboard-mockup.reveal.active:hover {
        transform: none !important;
      }

      .dash-caption {
        width: 100%;
        text-align: center;
      }

      .m-segments {
        height: auto;
        align-items: flex-start;
        flex-direction: column;
        padding: 16px;
      }
      .m-seg-header {
        margin-bottom: 12px;
      }
      .m-seg-list {
        flex-direction: column;
        align-items: flex-start;
        width: 100%;
      }
      .m-seg-item {
        padding: 12px 0;
        width: 100%;
        border-bottom: 1px solid rgba(255, 255, 255, 0.06);
      }
      .m-seg-item:last-child {
        border-bottom: none;
      }

      .roadmap-panel {
        padding: 24px;
      }
      .timeline {
        padding-left: 0;
      }
      .timeline::before {
        left: 3.5px;
      }
      .timeline-node {
        padding-left: 20px;
      }
      .timeline-node::before {
        left: 0px;
      }
      .node-desc {
        white-space: normal;
      }
      
      .section-divider-wrap .divider-pill {
        white-space: pre-wrap;
      }
      
      .site-footer {
        flex-direction: column;
        text-align: center;
        gap: 16px;
        padding: 24px;
      }
      .floating-wa {
        width: 52px;
        height: 52px;
        opacity: 1;
        pointer-events: auto;
      }
    }
    """

old_mobile_css_pattern = re.compile(r'@media\s*\(max-width:\s*767px\)\s*\{.*?(?=@media\s*\(max-width:\s*479px\))', re.DOTALL)
html = old_mobile_css_pattern.sub(mobile_css, html)

# FIX 3: Dashboard Interactive Tilt
tilt_script = """
      // Dashboard Interactive Tilt
      const mockupContainer = document.querySelector('.dashboard-wrapper');
      const mockup = document.querySelector('.dashboard-mockup');
      
      if (mockupContainer && mockup) {
        let isHovering = false;
        
        mockupContainer.addEventListener('mouseenter', () => {
          if (window.innerWidth >= 768) {
            isHovering = true;
            mockup.style.transition = 'transform 0.1s ease';
          }
        });
        
        mockupContainer.addEventListener('mousemove', (e) => {
          if (!isHovering) return;
          
          const rect = mockupContainer.getBoundingClientRect();
          const x = e.clientX - rect.left;
          const y = e.clientY - rect.top;
          
          const xPercent = (x / rect.width) - 0.5; // -0.5 to 0.5
          const yPercent = (y / rect.height) - 0.5; // -0.5 to 0.5
          
          const rotateX = -(yPercent * 16); // max +- 8 deg
          const rotateY = (xPercent * 12);  // max +- 6 deg
          
          mockup.style.transform = `rotateX(${rotateX - 4}deg) rotateY(${rotateY + 6}deg)`;
        });
        
        mockupContainer.addEventListener('mouseleave', () => {
          if (window.innerWidth >= 768) {
            isHovering = false;
            mockup.style.transition = 'transform 0.6s ease';
            mockup.style.transform = 'rotateX(-4deg) rotateY(6deg)';
            
            setTimeout(() => {
              if (!isHovering) mockup.style.transition = '';
            }, 600);
          }
        });
      }
"""
html = re.sub(
    r'(if\s*\(window\.innerWidth\s*<\s*768\)\s*\{\s*waBtn\.classList\.add\(\'visible\'\);\s*\})',
    r'\1\n' + tilt_script,
    html
)

# Apply 11px floor
html = re.sub(r'font-size:\s*8px;', 'font-size: 11px;', html)
html = re.sub(r'font-size:\s*9px;', 'font-size: 11px;', html)
html = re.sub(r'font-size:\s*10px;', 'font-size: 11px;', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixes applied.")
