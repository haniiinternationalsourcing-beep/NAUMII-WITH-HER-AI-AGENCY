# Jarvis AI Agency - Complete Architecture (Modules 01 to 31)

import sys
import content_creator
import ad_manager
import security_monitor
import social_scheduler
import seo_generator
import email_automation
import lead_generator
import script_writer
import text_to_video
import voiceover_synth
import thumbnail_creator
import ecommerce_copy
import support_bot
import sales_funnel
import competitor_analysis
import trend_predictor
import website_generator
import ui_ux_assistant
import brand_identity
import invoice_generator
import client_onboarding
import task_assigner
import analytics_reporter
import ai_copywriter
import chatbot_engine
import auto_blog
import influencer_outreach
import ab_testing
import saas_billing
import system_health
import master_command

MODULES = [
    "Automated Content Creation", "AI Ad Management", "Cybersecurity Monitoring",
    "Social Media Scheduler", "SEO Content Generator", "Email Marketing Automation",
    "Lead Generation Assistant", "AI Video Script Writer", "Text-to-Video Generator",
    "Voiceover Synthesis", "Thumbnail Creator", "E-Commerce Product Copywriter",
    "AI Customer Support Bot", "Sales Funnel Builder", "Competitor Analysis Tool",
    "Market Trend Predictor", "Website Code Generator", "UI/UX Layout Assistant",
    "Brand Identity Creator", "Automated Invoice Generator", "Client Onboarding System",
    "Project Task Auto-Assigner", "Data Analytics & Reporting", "AI Copywriting Assistant",
    "Chatbot Integration Engine", "Auto Blog Publisher", "Influencer Outreach Bot",
    "A/B Testing Analyzer", "SaaS Billing Integration", "System Health Checker",
    "Master AI Command Center"
]

def show_menu():
    print("=" * 50)
    print("        WELCOME TO JARVIS AI AGENCY SYSTEM        ")
    print("=" * 50)
    
    for idx, name in enumerate(MODULES, 1):
        print(f"[{idx:02d}] {name}")
        
    print("=" * 50)
    print("[00] Exit System")
    print("=" * 50)

def run_module(choice):
    if choice == 0:
        print("\nExiting Jarvis System. Goodbye!")
        sys.exit()
    elif choice == 1:
        topic = input("Enter Topic for Post Generation: ")
        content_creator.generate_post(topic)
    elif choice == 2:
        platform = input("Enter Platform (e.g. Facebook/Google): ")
        product = input("Enter Product/Service Name: ")
        ad_manager.create_ad_campaign(platform, product)
    elif choice == 3:
        domain = input("Enter Domain/IP to Scan: ")
        security_monitor.run_security_scan(domain)
    elif choice == 4:
        platform = input("Enter Platform (e.g. LinkedIn/Twitter): ")
        text = input("Enter Post Content: ")
        time_slot = input("Enter Time (e.g. Tomorrow 5 PM): ")
        social_scheduler.schedule_post(platform, text, time_slot)
    elif choice == 5:
        keyword = input("Enter Target Keyword: ")
        seo_generator.generate_seo_meta(keyword)
    elif choice == 6:
        r_type = input("Enter Target Audience (e.g. Startups/Freelancers): ")
        prod = input("Enter Product/Service: ")
        email_automation.create_email_campaign(r_type, prod)
    elif choice == 7:
        ind = input("Enter Industry/Niche: ")
        loc = input("Enter Location/City: ")
        lead_generator.find_leads(ind, loc)
    elif choice == 8:
        top = input("Enter Video Topic: ")
        plat = input("Enter Platform (e.g. YouTube Shorts/TikTok/Reels): ")
        script_writer.generate_video_script(top, plat)
    elif choice == 9:
        prompt = input("Enter Scene Description / Prompt: ")
        text_to_video.generate_video_prompt(prompt)
    elif choice == 10:
        text = input("Enter Core Message/Script: ")
        emotion = input("Enter Emotion/Tone (e.g. Emotional / Hustle / Deep): ")
        voiceover_synth.synthesize_voice(text, emotion)
    elif choice == 11:
        t_text = input("Enter Thumbnail Main Text/Title: ")
        t_style = input("Enter Visual Style (e.g. Minimalist / Clickbait / Tech Glow): ")
        thumbnail_creator.generate_thumbnail(t_text, t_style)
    elif choice == 12:
        prod = input("Enter Product Name: ")
        aud = input("Enter Target Audience (e.g. Gamers / Fitness Lovers): ")
        ecommerce_copy.generate_product_copy(prod, aud)
    elif choice == 13:
        query = input("Enter Customer Issue/Query: ")
        support_bot.handle_customer_query(query)
    elif choice == 14:
        b_type = input("Enter Business Type (e.g. Agency / SaaS / E-commerce): ")
        offer = input("Enter Core Offer/Product Name: ")
        sales_funnel.build_sales_funnel(b_type, offer)
    elif choice == 15:
        comp = input("Enter Competitor Brand/Website Name: ")
        ind = input("Enter Industry Niche: ")
        competitor_analysis.analyze_competitor(comp, ind)
    elif choice == 16:
        sec = input("Enter Industry/Market Sector: ")
        trend_predictor.predict_market_trends(sec)
    elif choice == 17:
        s_type = input("Enter Website Type (e.g. Portfolio / Agency Landing Page / Store): ")
        style = input("Enter Design Style (e.g. Minimalist Dark / Futuristic Neon / Clean Corporate): ")
        website_generator.generate_website(s_type, style)
    elif choice == 18:
        app = input("Enter App/Platform Type (e.g. SaaS Dashboard / Mobile App / Agency Site): ")
        palette = input("Enter Color Palette (e.g. Dark Neon / Minimalist Monochrome / Vibrant SaaS): ")
        ui_ux_assistant.design_layout(app, palette)
    elif choice == 19:
        b_name = input("Enter Brand Name: ")
        b_niche = input("Enter Business Niche/Industry: ")
        brand_identity.create_brand_identity(b_name, b_niche)
    elif choice == 20:
        c_name = input("Enter Client Name: ")
        inv_amount = input("Enter Total Invoice Amount ($): ")
        invoice_generator.generate_invoice(c_name, inv_amount)
    elif choice == 21:
        c_name = input("Enter Client Name: ")
        package = input("Enter Service Package (e.g. Full AI Agency Setup / Video Growth): ")
        client_onboarding.onboard_client(c_name, package)
    elif choice == 22:
        proj = input("Enter Project Name: ")
        members = input("Enter Team Members / Agents (e.g. Ali, Sara, AI-Bot): ")
        task_assigner.assign_tasks(proj, members)
    elif choice == 23:
        r_type = input("Enter Report Type (e.g. Social Media Growth / Sales & Revenue): ")
        timeframe = input("Enter Timeframe (e.g. Weekly / Monthly / Yearly): ")
        analytics_reporter.generate_report(r_type, timeframe)
    elif choice == 24:
        top = input("Enter Topic / Product Name: ")
        tone = input("Enter Tone (e.g. Professional / Aggressive Sales / Friendly & Engaging): ")
        ai_copywriter.generate_copy(top, tone)
    elif choice == 25:
        plat = input("Enter Integration Platform (e.g. Website Widget / WhatsApp / Telegram): ")
        persona = input("Enter Bot Persona / Tone (e.g. Helpful Support / Witty Sales Rep): ")
        chatbot_engine.deploy_chatbot(plat, persona)
    elif choice == 26:
        title = input("Enter Blog Title / Topic: ")
        cms = input("Enter Publishing Platform (e.g. WordPress / Ghost / Webflow): ")
        auto_blog.publish_blog(title, cms)
    elif choice == 27:
        handle = input("Enter Influencer Handle / Name (@username): ")
        offer = input("Enter Campaign Offer / Product: ")
        influencer_outreach.outreach_influencer(handle, offer)
    elif choice == 28:
        v_a = input("Enter Variant A (e.g. Headline A / Blue CTA Button): ")
        v_b = input("Enter Variant B (e.g. Headline B / Red CTA Button): ")
        metric = input("Enter Key Metric (e.g. Click-Through Rate / Signups): ")
        ab_testing.analyze_ab_test(v_a, v_b, metric)
    elif choice == 29:
        plan = input("Enter Subscription Plan (e.g. Pro Agency Tier / Starter / Enterprise): ")
        gw = input("Enter Payment Gateway (e.g. Stripe / PayPal / LemonSqueezy): ")
        saas_billing.manage_billing(plan, gw)
    elif choice == 30:
        system_health.check_system_health()
    elif choice == 31:
        master_command.launch_command_center()
    else:
        print("\n[-] Invalid selection! Please enter a valid module number.")

def main():
    while True:
        show_menu()
        try:
            user_input = int(input("\nEnter Module Number to Run (0 to Exit): "))
            run_module(user_input)
            input("\nPress Enter to return to main menu...")
        except ValueError:
            print("\n[-] Invalid input! Please enter a number.")
            input("\nPress Enter to try again...")

if __name__ == "__main__":
    main()

