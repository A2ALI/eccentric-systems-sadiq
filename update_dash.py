import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

css_to_add = """
    /* MOCKUP STYLES */
    .dashboard-mockup {
      --mk-dark: #0D0D0F;
      --mk-panel: #141418;
      --mk-card: #1A1A20;
      --mk-border: rgba(255, 255, 255, 0.08);
      --mk-border-strong: rgba(255, 255, 255, 0.12);
      --mk-text-pri: #E8E8EC;
      --mk-text-sec: #6B6B78;
      --mk-text-mut: #3A3A45;
      background-color: var(--mk-dark);
      border: 1px solid var(--light-border);
      border-radius: 8px;
      overflow: hidden;
      max-width: 900px;
      margin: 0 auto;
      transform-style: preserve-3d;
      transform: rotateX(-4deg) rotateY(6deg);
    }

    .m-topbar {
      height: 48px;
      background-color: var(--mk-dark);
      border-bottom: 1px solid var(--mk-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;
    }
    .m-topbar-left {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .m-logo {
      height: 16px;
      fill: var(--primary-green);
    }
    .m-title {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 400;
      font-size: 12px;
      color: var(--mk-text-pri);
    }
    .m-dot {
      color: var(--mk-text-mut);
      font-size: 10px;
    }
    .m-subtitle {
      font-family: 'Space Mono', monospace;
      font-size: 9px;
      color: var(--mk-text-sec);
    }
    .m-topbar-right {
      display: flex;
      gap: 6px;
    }
    .m-chrome-circle {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background-color: var(--mk-text-mut);
    }
    .m-body {
      display: flex;
    }
    .m-sidebar {
      width: 64px;
      background-color: var(--mk-dark);
      border-right: 1px solid var(--mk-border);
      display: flex;
      flex-direction: column;
      align-items: center;
      padding-top: 16px;
      gap: 8px;
    }
    .m-icon {
      width: 44px;
      height: 44px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 4px;
    }
    .m-icon svg {
      width: 16px;
      height: 16px;
      fill: var(--mk-text-sec);
    }
    .m-icon.active {
      background-color: rgba(45, 106, 53, 0.10);
    }
    .m-icon.active svg {
      fill: var(--primary-green);
    }

    .m-main {
      flex: 1;
      display: flex;
      flex-direction: column;
    }
    .m-metrics {
      height: 72px;
      display: flex;
      background-color: var(--mk-panel);
      border-bottom: 1px solid var(--mk-border);
    }
    .m-metric-block {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      border-right: 1px solid var(--mk-border);
    }
    .m-metric-block:last-child {
      border-right: none;
    }
    .m-metric-val {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 300;
      font-size: 22px;
      color: var(--mk-text-pri);
      line-height: 1.2;
    }
    .m-metric-val.gold {
      color: var(--gold);
    }
    .m-metric-label {
      font-family: 'Space Mono', monospace;
      font-size: 8px;
      color: var(--mk-text-sec);
      text-transform: uppercase;
      letter-spacing: 0.1em;
    }

    .m-middle {
      display: flex;
    }
    .m-panel-left {
      width: 55%;
      background-color: var(--mk-panel);
      border-right: 1px solid var(--mk-border);
      padding: 20px;
    }
    .m-panel-right {
      width: 45%;
      background-color: var(--mk-card);
      padding: 20px;
    }
    .m-panel-header {
      font-family: 'Space Mono', monospace;
      font-size: 9px;
      color: var(--mk-text-mut);
      letter-spacing: 0.2em;
      text-transform: uppercase;
      margin-bottom: 16px;
    }
    .m-camp-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 14px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }
    .m-camp-row:last-child {
      border-bottom: none;
    }
    .m-camp-name {
      font-family: 'Inter', sans-serif;
      font-size: 13px;
      color: var(--mk-text-pri);
      width: 40%;
    }
    .m-camp-status {
      font-family: 'Space Mono', monospace;
      font-size: 8px;
      border-radius: 100px;
      padding: 3px 10px;
      text-align: center;
    }
    .m-camp-status.green {
      background-color: rgba(45, 106, 53, 0.12);
      border: 1px solid rgba(45, 106, 53, 0.3);
      color: var(--primary-green);
    }
    .m-camp-status.gold {
      background-color: rgba(201, 169, 110, 0.10);
      border: 1px solid rgba(201, 169, 110, 0.3);
      color: var(--gold);
    }
    .m-camp-stats {
      display: flex;
      align-items: center;
      gap: 6px;
      width: 35%;
      justify-content: flex-end;
    }
    .m-camp-reach {
      font-family: 'Inter', sans-serif;
      font-size: 12px;
      color: var(--mk-text-sec);
    }
    .m-camp-cpa {
      font-family: 'Inter', sans-serif;
      font-size: 12px;
      color: var(--gold);
    }
    .m-camp-cpa.dash {
      color: var(--mk-text-mut);
    }

    .m-route-row {
      display: flex;
      align-items: center;
      padding: 16px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }
    .m-route-row:last-child {
      border-bottom: none;
    }
    .m-route-src {
      font-family: 'Inter', sans-serif;
      font-size: 12px;
      color: var(--mk-text-pri);
      width: 35%;
    }
    .m-route-dest-wrap {
      width: 35%;
      display: flex;
      flex-direction: column;
    }
    .m-route-dest {
      font-family: 'Space Mono', monospace;
      font-size: 10px;
      margin-bottom: 2px;
    }
    .m-route-dest.green {
      color: var(--primary-green);
    }
    .m-route-dest.gray {
      color: var(--mk-text-mut);
    }
    .m-route-sub {
      font-family: 'Space Mono', monospace;
      font-size: 8px;
      color: var(--mk-text-sec);
    }
    .route-arrow {
      flex: 1;
      height: 1px;
      background-color: rgba(255, 255, 255, 0.15);
      margin: 0 16px;
      position: relative;
    }
    .route-arrow::after {
      content: "";
      position: absolute;
      right: 0;
      top: -3px;
      width: 6px;
      height: 6px;
      border-top: 1px solid rgba(255, 255, 255, 0.15);
      border-right: 1px solid rgba(255, 255, 255, 0.15);
      transform: rotate(45deg);
    }

    .m-segments {
      height: 64px;
      background-color: var(--mk-dark);
      border-top: 1px solid var(--mk-border);
      padding: 0 16px;
      display: flex;
      align-items: center;
    }
    .m-seg-header {
      font-family: 'Space Mono', monospace;
      font-size: 9px;
      color: var(--mk-text-sec);
      width: 140px;
    }
    .m-seg-list {
      flex: 1;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .m-seg-item {
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }
    .m-seg-text {
      display: flex;
      flex-direction: column;
    }
    .m-seg-name {
      font-family: 'Inter', sans-serif;
      font-size: 11px;
      color: var(--mk-text-pri);
      margin-bottom: 2px;
    }
    .m-seg-status {
      font-family: 'Space Mono', monospace;
      font-size: 8px;
    }
    .m-seg-status.green {
      color: var(--primary-green);
    }
    .m-seg-status.gold {
      color: var(--gold);
    }
    .pulse-dot.green-dot {
      width: 6px;
      height: 6px;
      background-color: var(--primary-green);
      border-radius: 50%;
      animation: mk-pulse 2s infinite;
      margin-top: 4px;
    }
    .static-dot.gold-dot {
      width: 6px;
      height: 6px;
      background-color: var(--gold);
      border-radius: 50%;
      margin-top: 4px;
    }
    @keyframes mk-pulse {
      0% { box-shadow: 0 0 0 0 rgba(45, 106, 53, 0.7); }
      70% { box-shadow: 0 0 0 4px rgba(45, 106, 53, 0); }
      100% { box-shadow: 0 0 0 0 rgba(45, 106, 53, 0); }
    }
"""

mobile_css_to_add = """
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
"""

new_html_content = """
      <div class="dashboard-mockup reveal">
        <div class="m-topbar">
          <div class="m-topbar-left">
            <svg class="m-logo" viewBox="0 0 1350 1252" xmlns="http://www.w3.org/2000/svg">
              <path d="M455.5 260.4c-2.7.7-6.5 2-8.4 3-5.4 2.9-13 11.1-15.9 17.4-2.3 4.9-2.7 7-2.7 14.7 0 7.9.4 9.7 2.9 14.9 3.7 7.6 9.6 13.5 17.2 17.2 5.3 2.6 6.9 2.9 15.4 2.9 7.6 0 10.4-.5 14.2-2.2 7.2-3.3 14.6-10.8 17.9-18.1l2.8-6.2 47.8.2 47.8.3.3 11.3c.3 12.9.7 12.4-10.3 13.6-14.6 1.6-28.8 8.5-41.4 20.1-7 6.6-12.1 13.6-17.3 24-4.3 8.6-5.7 12.7-7.2 21.9l-1.2 7.1-12.5-.3c-13.6-.4-19.2.6-31.8 5.7-10.1 4.1-19 10.2-26.4 18-15.4 16.4-22.9 33.6-24.4 56.4l-.6 9.7-36.6-.2-36.6-.3-.3-52.5-.2-52.5 6.5-2.9c7.3-3.2 13.4-9.2 17.5-17.2 3.6-7.1 4-19.6.9-27.9s-12.1-17.3-20.4-20.4c-8.8-3.3-20.8-2.7-28.4 1.4-14.1 7.7-21.9 23.1-19.1 37.9 2.4 12.7 10.9 23.4 21.5 26.9l4 1.4.5 58.6.5 58.7 2.8 2.7 2.7 2.8 42.3.1c23.2.1 43.2.2 44.4.3 1.6.1 2.5 1.1 3.3 3.8 1.8 5.6 8.7 18.2 12.7 23 1.9 2.4 3.2 4.7 2.9 5.2s-2.7 1.4-5.2 2c-5.5 1.4-16.6 6.8-22.6 10.9-5.2 3.6-15.3 14.1-19.5 20.2-9.4 13.8-14.1 27.8-15 44.7l-.6 11.3h-18.3l-1.3-3.8c-2.1-5.8-6.6-11.7-11.8-15.5-8.8-6.3-11-7.1-21.3-7.1-8.1-.1-10.2.3-14.3 2.3-7.5 3.7-14 10.2-17.8 17.8-3 6.1-3.3 7.7-3.4 15.3 0 7.7.3 9.1 3.5 15.3 3.7 7.5 8.5 12.3 16.5 16.5 4.5 2.4 6.1 2.7 15 2.7 11.9-.1 16.7-1.8 24.3-8.9 4.2-4 6.2-6.9 10.2-15.6.6-1.2 3.1-1.6 11.9-1.8 10.7-.3 11.3-.2 11.8 1.8 1.1 4.3 7.6 16.6 11.8 22.6 9 12.6 24.4 24.2 37.5 28.4 3.6 1.1 7.1 2.2 7.8 2.5.9.3-.4 2.9-4.2 8.3-13.5 19.2-18 44.4-12.1 67.8 2.6 10.4 8.7 23.8 13.3 29.1 1.5 1.7 4.4 5.2 6.5 7.7 7.1 8.6 19.6 16.5 33.7 21.2 7.8 2.7 9.7 2.9 23.3 2.9h14.8l-.3 4.5-.3 4.5-74.8.3-74.7.2-2.7-5.7c-6.2-13.1-18.5-21.3-32-21.3-8.3 0-13.4 1.5-19.9 5.7-6.3 4.1-9.9 8.2-13.3 15.3-2.2 4.7-2.6 6.8-2.6 14.5 0 7.8.4 9.7 2.8 14.7 3.7 7.5 12.8 16 19.9 18.4 3.6 1.3 7.8 1.8 13.3 1.8 10.1-.2 17-3.1 24-10.1 5-5 6.2-6.7 8.9-13.6l1.5-3.7H448v56.8l-5.4 2.2c-6.4 2.5-14.1 10.1-17.4 17-4.3 9-4.4 21.3-.3 30.6 2.8 6.2 10.3 13.7 16.9 17.1 5.1 2.5 6.8 2.8 15.2 2.8 11.4 0 16.2-1.8 24.1-9.2 15.2-14.2 15.4-36.7.4-51.8-3.1-3.2-6.9-5.8-10-6.9-2.7-1.1-5.2-2.3-5.5-2.7s-.3-13 0-28.1l.5-27.3 26.6-.3 26.6-.2 2.3 6.2c4.6 12.7 15 27.1 26.6 36.6 10.5 8.6 27.9 15.6 41.9 16.8 8.8.8 22.8-1 31-4 19.8-7.2 38.7-25.2 46.6-44.6 5.3-13 5.9-19.1 5.9-56 0-31.5-.1-33.8-1.9-35.8-2.7-3.2-9-3-12.2.4l-2.4 2.6-.5 35.1c-.6 32.6-.8 35.7-2.8 41.7-5.4 16.2-17.3 30.1-31.3 36.8-10.5 5-17.2 6.6-27.5 6.4-32.8-.4-60.4-28.6-60.7-62.1-.1-12.6.4-13.9 8.1-19.4 16.2-11.8 28.8-31.9 32.8-52.5 2.3-12.2 1.6-20-2-22.4-.6-.4-3-.8-5.3-.8-5.2 0-8.3 3.3-8.3 9 0 5.3-2.5 17.6-4.6 23-4.5 11.5-16.8 26.6-26.2 32.4-9.6 5.8-18.2 8.1-29.7 8-15.4-.1-26.5-4.9-39.7-17.3-6.7-6.3-8.6-8.8-12.3-16.5-5.4-11.3-7.5-19.9-7.5-30.2 0-21.2 9.8-40.7 27.2-54 6.4-5 7.7-7.8 5.8-12.5-1.7-3.9-4.4-4.9-13.7-4.9-24.7 0-46.8-15.5-56.7-39.8-11.5-28.5-1.8-62.4 22.8-79.6 11.5-8 18.2-10.1 32.6-10 10.4 0 12.2.3 19 3 13.7 5.5 24.1 15.2 31.7 29.7 4.2 7.9 6.1 14.2 7.4 24.2.6 4.4 1.5 9.2 2 10.7 1.8 4.5 9.5 5.3 13.4 1.3 2.1-2 2.5-3.4 2.5-8 0-18.4-9.8-41.1-23.8-55.5-10.7-10.9-22.2-17.9-34.7-20.9-7.7-1.9-12.1-4.9-18.7-12.6-12.1-14.3-17.5-30-16.5-47.9 1.2-20 9.3-36.5 24-48.8 6.6-5.4 10.6-7.7 19.8-11 5.3-1.9 8.4-2.3 17.9-2.3 12.1 0 16 1.1 16 4.3 0 3.8 3.2 13.9 6.9 21.6 7.8 16.6 19.3 28.2 35.6 36.1 11 5.4 19 7.5 29 7.7 8.8.1 11.2-1.3 12.1-7.3.5-2.7.1-3.9-1.8-6-2-2.1-3.8-2.8-10.9-3.7-4.7-.6-11.4-2.1-15-3.3-16.4-5.6-30.7-20.7-37-38.9-3-8.6-3.2-27.1-.5-37 2.8-10.2 9.2-21.5 16.1-28.5 8.1-8.1 13.2-11.5 23.5-15.5 8.2-3.1 8.9-3.2 20.5-2.8 10.7.4 12.8.8 19.7 3.7 18 7.6 29.7 20.9 37.6 42.5 2.5 7 2.6 7.6 3.1 42.6.6 37.2.8 38.7 5.2 41.1 3.1 1.6 8.4.3 10.3-2.6 2.3-3.5 2.4-64.3 0-76.5-3.3-17.5-10.2-31.4-21.6-43-11.1-11.4-20.3-17.6-31.8-21.5l-6.5-2.2-.5-19.1c-.5-18.3-.6-19.3-2.8-21.4l-2.3-2.3-54.3-.3-54.4-.2-1.9-5.2c-3.5-10-14.6-19.2-26.3-21.8-5.7-1.2-8.2-1.1-14.5.4m16.5 18.5c6 3.2 9.3 8.3 9.8 15 .5 7.3-1.6 12.2-7 16.1-7 5.1-16.3 4.8-22.9-.7-4.1-3.5-5.9-7.9-5.9-14.4 0-6.9 2.4-11.6 7.9-15 5.5-3.5 12.7-3.9 18.1-1m-124.7 55.2c17 8.7 12.7 33.3-6.2 35.6-19 2.2-26.9-24.9-10.1-34.6 3.9-2.3 12.7-2.8 16.3-1m-15.2 287.1c14.4 4.9 17.4 23.2 5.3 32.4-4.8 3.7-12.4 4.4-18.5 1.7-8.9-3.9-13.3-15.6-9.1-23.9 4.7-9.1 13.6-13.2 22.3-10.2m6.6 218.9c7 2.6 11.7 10.5 11.1 18.5-1.1 13.6-14.1 21.1-26.4 15.2-10.5-4.9-13.6-18.9-6.2-28.4 4.3-5.3 14.6-7.9 21.5-5.3m127.7 100.4c7 4.1 10.6 12.7 8.6 20.7-1.4 5.4-4.9 9.4-10.4 11.9-5 2.3-9.5 2.4-14.4.4-7.7-3.3-11.2-8.6-11.2-17 0-6.2 1.4-9.7 5.7-13.7 5.8-5.5 14.6-6.4 21.7-2.3"/>
              <path d="M992 263.4c-11.1 2.5-19.5 9.2-24.8 19.5-2.4 4.8-2.7 6.6-2.7 15 0 7.9.4 10.5 2.3 14.5 3.8 8.4 8.6 13.2 16.8 17.2l7.4 3.5v58.4c0 52.2-.2 58.3-1.6 58.9-2.2.9-51.7.7-53-.2-.6-.4-2.6-3.5-4.4-7-7.4-14-23.5-28.8-37.5-34.7-3.9-1.6-7.6-3.3-8.2-3.8-1-.7-1.3-9.1-1.3-35.8v-34.8l7.5-3.6c5.9-2.8 8.3-4.7 11.4-8.8 8.5-11.3 10.2-25.1 4.7-37.3-5.3-11.5-14.7-18.5-27.8-20.6-11.9-1.8-21.7 1.9-30.6 11.6-6.9 7.5-8.7 12.4-8.6 23.6 0 8.3.4 10.2 2.8 15.4 3.6 7.5 9.2 12.8 17.2 16.7l6.4 3v33.4c0 18.4-.3 33.6-.7 33.8-.5.3-4.8.6-9.7.8l-8.9.4-1.8-8.3c-5-22.9-17.3-41.3-35.6-53.3-19.1-12.4-40.1-15.5-62.3-9.2-19.5 5.5-39.5 23.3-49 43.5-7.8 16.9-8.3 19.8-8.7 60.1l-.4 35.7 3 3c3.8 3.8 7.8 4 11.2.4l2.4-2.6.5-34.6c.6-33.4.7-35 3.1-42.8 4.8-15.4 16.6-32.1 27.8-39.3 2.6-1.7 8.6-4.5 13.2-6.2 7.3-2.7 9.7-3.2 18.4-3.2 15.4 0 27.5 4.9 39.5 16 30.1 27.8 27.8 76.8-4.5 99.9-8.6 6.1-16.5 9.1-27.4 10.5-11.2 1.4-14.1 3.3-14.1 8.8 0 2.7.7 4.4 2.4 6.1 2.2 2 3.5 2.2 10 2.2 8.2-.1 13.1-1.1 21.6-4.4 24.6-9.6 42.6-30.4 48.6-56 1.1-4.8 2.4-8 3.3-8.4 3.4-1.3 18.3-1.6 24.3-.5 7.8 1.5 20.8 7.7 27 12.9 11.1 9.3 19.2 22.2 22.4 35.9 2 8.2 2.2 22.6.5 30.8-2.7 12.8-10.4 26-20.6 35.3-4.7 4.3-6.9 5.5-14.3 7.7-13.5 4.1-24.6 11-35 21.5-12.7 13-22.1 35.7-22.2 53.6 0 6.1.3 7.3 2.3 9.2 3 2.8 8.6 2.9 11.5.2 1.1-1.1 2.4-3.7 2.7-5.7 3.6-23.9 7.5-33.3 18.8-45.9 23.7-26.3 64.7-23.8 86.5 5.3 10.5 13.9 13.7 23.6 13.6 41.8 0 11.4-.4 13.9-2.6 20.3-2.9 8-10 20-15 25.4-11.7 12.3-27.1 18.8-44.6 18.8-7.5 0-8.5.2-10.7 2.5-3.7 3.7-3.4 8.7.8 12.2 10.6 8.9 19.4 19.1 23 26.5 12.5 25.9 7.9 56.5-11.3 75.9-12.6 12.7-25.8 18.4-42 18.3-21.1-.2-39.4-11.8-51.3-32.4-3.9-6.8-6.4-15.5-7.6-25.9-1.3-11.4-3.1-14.1-9.6-14.1-7.9 0-9.7 5.5-7.1 20.7 4.1 23.5 18 45.5 36.1 56.9 4.1 2.7 4.5 3.2 5.1 8.3 1.6 13-1.9 29.3-8.8 40.8-7 11.7-19.9 22.6-31.9 27.1-32.2 11.9-66.7-5.8-79-40.8-2.2-6.2-2.3-8.3-2.8-41.6-.6-32.8-.7-35.3-2.5-37.3-1.4-1.5-3.1-2.1-6.2-2.1-3.6 0-4.6.5-6.3 2.9-2 2.8-2.1 4.2-2.1 35.4 0 29.6.2 33.4 2.1 41.9 3.6 15.5 9.1 25.8 19.8 37.2 10.3 10.8 21.1 18 32.6 21.7 3.9 1.2 7.3 2.7 7.7 3.3s.8 8.4.8 17.3v16.2l2.6 2c2.6 2.1 3.3 2.1 74.5 2.1H903l2.7 5.5c3.6 7.8 10.3 14.9 17.1 18.2 5.2 2.5 6.7 2.8 16.2 2.8 10.3-.1 10.6-.1 16.6-3.8 7.4-4.4 11.8-9.2 15.3-16.7 2.2-4.6 2.6-6.9 2.6-14.5s-.4-9.9-2.6-14.6c-3.6-7.7-9.1-13.4-16.3-17.2-5.7-3-6.8-3.2-16.1-3.2-9 .1-10.6.4-15.3 2.8-7.1 3.7-14.5 11.5-17.3 18.3l-2.3 5.4H771v-19.7l8.8-1.2c26-3.6 49.2-21.5 61.1-47.3 4.9-10.5 6.2-15.8 7-28.3l.6-10 3.5.5c1.9.3 8.9.5 15.5.4 11.2-.1 12.6-.3 21.2-3.6 11.3-4.3 18.7-8.7 26.5-15.7 30.5-27.6 36.2-72.9 13.5-108.3-2-3.1-4.1-5.9-4.7-6.3-2.4-1.5-.6-3.3 5.1-4.9 19.2-5.3 38.6-22.1 47.2-40.9l1.7-3.7h49v106.8l-2.6.6c-3.4.9-12.3 6.6-15 9.7-6.8 7.8-10.1 19.4-8.4 29.2q3.45 19.2 21 27.6c4.7 2.2 6.7 2.6 14.5 2.5 11.1-.2 16.2-2.4 24.7-10.9 7.4-7.4 10.1-14 10-24.5 0-9.4-2.7-17-8.4-23.5-4.1-4.7-12.9-10.5-15.9-10.5-.9 0-2-.7-2.3-1.6s-.6-27.6-.6-59.5v-58l-2.5-2.4c-1.3-1.4-3.4-2.5-4.7-2.5-1.3-.1-13.5-.2-27.3-.3l-25-.2.3-13.5c.5-17.1-1.5-25.8-9.4-41.8-4.8-9.7-6.8-12.5-14.2-20-10.2-10.3-21.2-17.3-31.3-19.9-3.8-.9-6.9-2.1-6.9-2.6 0-.4 2.2-4 4.9-8 6-8.9 9.4-16.2 12.3-26.3 1.9-6.7 2.3-10.2 2.2-23.2V468h28.9c31.4 0 33.8-.4 35.7-5.6.6-1.5 1-28 1-66V333l6.3-2.8c11.3-5.2 19.4-17 20.5-29.8 1.2-15.4-9.5-31.8-23.8-36.2-5.9-1.8-13.2-2.1-19-.8M881.2 281c7.6 2.2 13.8 10.2 13.8 18 0 4.7-2.6 10.4-6.4 13.9-2.5 2.3-11.5 5.4-13.9 4.6-.7-.2-2.4-.6-3.9-.9-3.7-.8-8.5-5.1-10.8-9.7-5.3-10.2 1-23.2 12.4-26 4.4-1 4.7-1 8.8.1m125.5.1c6.8 2.6 10.5 8.6 10.4 17.1 0 7.6-3 12.6-9.3 15.7-16.6 8-32.5-7.8-24.7-24.4 2.8-6 8.5-9.5 15.6-9.5 2.8 0 6.4.5 8 1.1m36 498.4c8.1 3.4 11.7 9.7 11.1 19.1-.5 7.9-4.1 13-11.1 15.6-12.8 4.8-25.2-4.3-25-18.1.2-6.8 3.8-12.4 10.2-15.8 5.1-2.7 9.7-2.9 14.8-.8M949 938.4c10.9 7.2 10.5 23.5-.7 30.7-4.3 2.7-5.5 3-10.9 2.7-7.5-.5-12.1-3.5-15.3-10.1-6.4-13.2 3-27.4 17.6-26.4 3.5.2 6.5 1.2 9.3 3.1"/>
              <path d="M633 492.1c-2.5 2.1-2.5 2.3-2.8 20.4l-.3 18.3-13.2.4c-11.5.3-13.8.6-17.7 2.6-5.8 3-9.5 6.6-12.8 12.2-2.5 4.2-2.7 5.5-3.2 20l-.5 15.5h-13c-19.2.1-20.2.2-22.5 2.7s-2.7 8.3-.7 10.9c2.6 3.4 5.5 3.9 21.1 3.9H583v23h-16.5c-16.3 0-16.6 0-19 2.5-2.7 2.7-3.3 7.9-1.2 10.6 2.6 3.4 5.5 3.9 21.1 3.9H583v23h-15.5c-20 0-22.5 1.1-22.5 9.5 0 2.4-.7 3.9-2.6 5.4 2.5 1.9 4 2.1 18.9 2.1h16.3l.4 11.2c.4 13 2.4 18.4 9.1 24.5 6.4 5.7 9.7 6.7 24.2 7.3l13 .5.5 17.8.5 17.9 2.8 2.4c3.1 2.6 5.7 3 9 1.2 4.4-2.3 4.6-3.5 4.7-22.1v-17.8l11.3.3 11.2.3.5 18.2c.3 10 .7 18.3 1 18.6 5.5 4.5 9.1 4.7 13.1.8l2.9-2.9V722h21.7l.5 18c.5 19.7 1 21.2 6.8 22.5 3.6.8 8.6-1.7 9.6-4.7.4-1.3.8-9.5.9-18.3s.3-16.3.4-16.8c0-.4 5.5-.7 12.1-.7 14.2 0 20.5-1.9 26.2-7.7 6.4-6.5 8.1-11.9 8.6-27.1l.5-13.2h16.2c15.8 0 16.3-.1 18.9-2.5 3.7-3.4 3.7-9.5 0-12.4-2.5-1.9-4-2.1-19-2.1H774v-23h15.5c20 0 22.5-1.1 22.5-9.5 0-2.4-.7-3.9-2.6-5.4-2.5-1.9-4-2.1-19-2.1H774v-23h16.5c16.3 0 16.6 0 19-2.5 3.4-3.3 3.4-8.7 0-12-2.4-2.5-2.7-2.5-18.8-2.5h-16.4l-.5-12.3c-.8-17.6-4.6-25-15.6-30.4-5.1-2.5-7-2.9-18.7-3.3l-13-.5-.3-18.2-.2-18.2-2.7-2c-3.4-2.8-7.6-2.6-11 .3l-2.8 2.4-.2 17.4c-.1 9.5-.2 17.6-.3 18 0 .5-4.9.8-11 .8h-11v-17.1c0-17.2-.5-20-3.9-22.6-2.7-2.1-7.9-1.5-10.6 1.2-2.5 2.4-2.5 2.6-2.5 20.5v18h-23v-18c0-17.9 0-18.1-2.5-20.5-3-3.1-8-3.2-11.5-.4M751.7 550c1.8 1.1 3.6 3.2 4 4.7 1 3.7 1 139.9 0 143.6-.4 1.5-2.2 3.6-4 4.7-3.1 1.9-5.4 2-73.7 2-63.6 0-70.8-.2-72.9-1.6-5.1-3.6-5.1-3.2-5.1-77.1 0-63.5.1-69.1 1.8-72.3.9-1.9 2.8-4 4.2-4.7 1.9-1 18.5-1.3 72.5-1.3 67.8 0 70.1.1 73.2 2m-131.9 16.9-3.3 2.9v114.4l2.8 2.4 2.8 2.4h112.6l2.7-2.5 2.6-2.4v-56.6c0-36.9-.4-57.3-1-58.6-2.7-4.9-3.1-4.9-61.4-4.9H623zM723 582.2v89.3h-89.5l-.3-44c-.1-24.2 0-44.6.3-45.3.3-.9 10.3-1.2 45-1.2 34.9 0 44.5.3 44.5 1.2"/>
            </svg>
            <div class="m-title">ECCENTRIC SYSTEMS</div>
            <div class="m-dot">·</div>
            <div class="m-subtitle">SWIFT CONSULT</div>
          </div>
          <div class="m-topbar-right">
            <div class="m-chrome-circle"></div>
            <div class="m-chrome-circle"></div>
            <div class="m-chrome-circle"></div>
          </div>
        </div>
        <div class="m-body">
          <div class="m-sidebar">
            <div class="m-icon"><svg viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg></div>
            <div class="m-icon active"><svg viewBox="0 0 24 24"><path d="M21.69 11.51l-4.48-1.5V6a2 2 0 00-2-2h-3L7.79 6.22H3v9.55h4.79L12.21 18h3a2 2 0 002-2v-4l4.48-1.5a1 1 0 000-1.89zM15.21 14h-3L8.63 12H5V8h3.63l3.58-2h3v8z"/></svg></div>
            <div class="m-icon"><svg viewBox="0 0 24 24"><circle cx="9" cy="8" r="4"/><path d="M9 14c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/><circle cx="16" cy="8" r="3"/><path d="M16 14c-1.4 0-3.83.6-5.35 1.63A5.5 5.5 0 0 1 12 18v2h9v-2c0-2.66-5.33-4-8-4z"/></svg></div>
            <div class="m-icon"><svg viewBox="0 0 24 24"><path d="M3 4l8 10.33V20l2 2v-7.67L21 4H3z"/></svg></div>
            <div class="m-icon"><svg viewBox="0 0 24 24"><path d="M3.5 18.5l6-6 4 4 8-8V11l-8 8-4-4-6 6z"/></svg></div>
          </div>
          <div class="m-main">
            <div class="m-metrics">
              <div class="m-metric-block">
                <div class="m-metric-val">3</div>
                <div class="m-metric-label">CAMPAIGNS ACTIVE</div>
              </div>
              <div class="m-metric-block">
                <div class="m-metric-val">12</div>
                <div class="m-metric-label">CONTENT LIVE</div>
              </div>
              <div class="m-metric-block">
                <div class="m-metric-val">47</div>
                <div class="m-metric-label">LEADS THIS WEEK</div>
              </div>
              <div class="m-metric-block">
                <div class="m-metric-val gold">$18.40</div>
                <div class="m-metric-label">AVG COST PER LEAD</div>
              </div>
            </div>
            <div class="m-middle">
              <div class="m-panel-left">
                <div class="m-panel-header">ACTIVE CAMPAIGNS</div>
                
                <div class="m-camp-row">
                  <div class="m-camp-name">Rental — Zamalek</div>
                  <div class="m-camp-status green">RUNNING</div>
                  <div class="m-camp-stats">
                    <span class="m-camp-reach">8.4K</span>
                    <span class="m-dot">·</span>
                    <span class="m-camp-cpa">$14.20</span>
                  </div>
                </div>
                
                <div class="m-camp-row">
                  <div class="m-camp-name">Investment — New Capital</div>
                  <div class="m-camp-status green">RUNNING</div>
                  <div class="m-camp-stats">
                    <span class="m-camp-reach">12.1K</span>
                    <span class="m-dot">·</span>
                    <span class="m-camp-cpa">$22.80</span>
                  </div>
                </div>
                
                <div class="m-camp-row">
                  <div class="m-camp-name">Brand — Cairo Lifestyle</div>
                  <div class="m-camp-status gold">OPTIMISING</div>
                  <div class="m-camp-stats">
                    <span class="m-camp-reach">31.2K</span>
                    <span class="m-dot">·</span>
                    <span class="m-camp-cpa dash">—</span>
                  </div>
                </div>
                
              </div>
              <div class="m-panel-right">
                <div class="m-panel-header">LEAD ROUTING</div>
                
                <div class="m-route-row">
                  <div class="m-route-src">Rental Leads</div>
                  <div class="route-arrow"></div>
                  <div class="m-route-dest-wrap">
                    <div class="m-route-dest green">/rentals</div>
                    <div class="m-route-sub">23 leads this week</div>
                  </div>
                </div>
                
                <div class="m-route-row">
                  <div class="m-route-src">Investment Leads</div>
                  <div class="route-arrow"></div>
                  <div class="m-route-dest-wrap">
                    <div class="m-route-dest green">/investments</div>
                    <div class="m-route-sub">14 leads this week</div>
                  </div>
                </div>
                
                <div class="m-route-row">
                  <div class="m-route-src">Brand Traffic</div>
                  <div class="route-arrow"></div>
                  <div class="m-route-dest-wrap">
                    <div class="m-route-dest gray">/</div>
                    <div class="m-route-sub">10 this week</div>
                  </div>
                </div>
                
              </div>
            </div>
            <div class="m-segments">
              <div class="m-seg-header">ACTIVE SEGMENTS</div>
              <div class="m-seg-list">
                <div class="m-seg-item">
                  <div class="pulse-dot green-dot"></div>
                  <div class="m-seg-text">
                    <div class="m-seg-name">Nigerian Diaspora (UK)</div>
                    <div class="m-seg-status green">ACTIVE</div>
                  </div>
                </div>
                <div class="m-seg-item">
                  <div class="pulse-dot green-dot"></div>
                  <div class="m-seg-text">
                    <div class="m-seg-name">Gulf-Based Investors</div>
                    <div class="m-seg-status green">ACTIVE</div>
                  </div>
                </div>
                <div class="m-seg-item">
                  <div class="static-dot gold-dot"></div>
                  <div class="m-seg-text">
                    <div class="m-seg-name">Cairo Short-Stay Travelers</div>
                    <div class="m-seg-status gold">LEARNING</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
"""

new_caption_content = '<div class="dash-caption reveal">One screen. Content, campaigns, audiences, and funnel routing — visible and controllable from a single dashboard.</div>'

# CSS Injection: We remove old dashboard css and add new css.
# Old dashboard css was between /* DASHBOARD MOCKUP */ and /* STORY PANELS / ROADMAP */
css_pattern = re.compile(r'/\*\s*DASHBOARD MOCKUP\s*\*/.*?(?=\/\*\s*STORY PANELS \/ ROADMAP\s*\*\/)', re.DOTALL)
html = css_pattern.sub(f'/* DASHBOARD MOCKUP */\n{css_to_add}\n\n', html)

# Mobile CSS Injection: we need to remove the old mobile dashboard overrides and add the new one.
# They are inside @media (max-width: 767px)
mobile_css_pattern = re.compile(r'\.dashboard-mockup\s*\{\s*transform:\s*none\s*!important;\s*border-radius:\s*4px;\s*min-width:\s*800px;\s*\}\s*\.dashboard-mockup\.reveal\s*\{\s*transform:\s*translateY\(28px\)\s*!important;\s*\}\s*\.dashboard-mockup\.reveal\.active\s*\{\s*transform:\s*translateY\(0\)\s*!important;\s*\}\s*\.dashboard-mockup\.reveal\.active:hover\s*\{\s*transform:\s*none\s*!important;\s*\}')
html = mobile_css_pattern.sub(f'.dashboard-mockup {{\n        transform: none !important;\n        border-radius: 4px;\n        min-width: 800px;\n      }}\n      .dashboard-mockup.reveal {{\n        transform: translateY(28px) !important;\n      }}\n      .dashboard-mockup.reveal.active {{\n        transform: translateY(0) !important;\n      }}\n      .dashboard-mockup.reveal.active:hover {{\n        transform: none !important;\n      }}\n{mobile_css_to_add}', html)

# HTML Block Injection:
# Replace <div class="dashboard-mockup reveal">...</div> and <div class="dash-caption reveal">...</div>
html_pattern = re.compile(r'<div class="dashboard-wrapper">\s*<div class="dashboard-mockup reveal">.*?</div>\s*</div>\s*<div class="dash-caption reveal">.*?</div>', re.DOTALL)
html = html_pattern.sub(f'<div class="dashboard-wrapper">\n{new_html_content}\n    </div>\n    {new_caption_content}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done!')
