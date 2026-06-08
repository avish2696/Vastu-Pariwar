#!/usr/bin/env python3
"""
Vastu Pariwar Website Setup Verification Script
Checks if all files are properly configured
"""

import os
import sys

def check_file_exists(filepath, description):
    """Check if a file exists and print status"""
    exists = os.path.exists(filepath)
    status = "✅" if exists else "❌"
    print(f"{status} {description}: {filepath}")
    return exists

def check_css_content(filepath):
    """Check if CSS file has proper content"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            has_colors = '--color-primary' in content
            has_utilities = '.bg-primary' in content
            has_typography = '.font-headline-xl' in content
            
            if has_colors and has_utilities and has_typography:
                print("✅ CSS file has all required content")
                return True
            else:
                print("❌ CSS file is missing some content")
                if not has_colors:
                    print("   Missing: CSS color variables")
                if not has_utilities:
                    print("   Missing: Utility classes")
                if not has_typography:
                    print("   Missing: Typography classes")
                return False
    except Exception as e:
        print(f"❌ Error reading CSS: {e}")
        return False

def check_html_tailwind(filepath):
    """Check if HTML has Tailwind CDN"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            has_tailwind = 'cdn.tailwindcss.com' in content
            
            if has_tailwind:
                print(f"✅ {os.path.basename(filepath)} has Tailwind CDN")
                return True
            else:
                print(f"❌ {os.path.basename(filepath)} missing Tailwind CDN")
                return False
    except Exception as e:
        print(f"❌ Error reading HTML: {e}")
        return False

def main():
    print("=" * 60)
    print("🏠 VASTU PARIWAR WEBSITE VERIFICATION")
    print("=" * 60)
    print()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("📁 CHECKING FILE STRUCTURE")
    print("-" * 60)
    
    files_to_check = [
        (os.path.join(base_dir, "index.html"), "Main HTML"),
        (os.path.join(base_dir, "css", "style.css"), "Main CSS"),
        (os.path.join(base_dir, "js", "main.js"), "Main JavaScript"),
        (os.path.join(base_dir, "pages", "home.html"), "Home Page"),
        (os.path.join(base_dir, "pages", "about.html"), "About Page"),
        (os.path.join(base_dir, "pages", "services.html"), "Services Page"),
        (os.path.join(base_dir, "pages", "contact.html"), "Contact Page"),
    ]
    
    all_exist = True
    for filepath, description in files_to_check:
        if not check_file_exists(filepath, description):
            all_exist = False
    
    print()
    print("🎨 CHECKING CONTENT IMAGES")
    print("-" * 60)
    
    images = [
        "a_beautiful_modern_indian_house_exterior_at_dusk_warm_lighting_elegant_screen.png",
        "a_happy_indian_family_in_a_cozy_well_lit_living_room_laughing_together_feeling_screen.png",
        "a_happy_indian_family_standing_in_front_of_a_beautiful_modern_home_sunlight_screen.png",
        "a_professional_female_vastu_consultant_in_business_casual_attire_pointing_at_a_screen.png",
        "a_professional_vastu_consultant_pointing_at_a_blueprint_on_a_table_in_a_modern_screen.png",
    ]
    
    images_exist = 0
    for img in images:
        img_path = os.path.join(base_dir, "images", img)
        if check_file_exists(img_path, "Image"):
            images_exist += 1
    
    print()
    print("🔍 CHECKING CSS CONFIGURATION")
    print("-" * 60)
    css_ok = check_css_content(os.path.join(base_dir, "css", "style.css"))
    
    print()
    print("🔗 CHECKING TAILWIND CDN INTEGRATION")
    print("-" * 60)
    tailwind_ok = check_html_tailwind(os.path.join(base_dir, "index.html"))
    
    print()
    print("=" * 60)
    print("📊 VERIFICATION SUMMARY")
    print("=" * 60)
    print(f"Files present: {len([f for f, _ in files_to_check if os.path.exists(f)])}/{len(files_to_check)}")
    print(f"Images present: {images_exist}/{len(images)}")
    print(f"CSS configured: {'✅ Yes' if css_ok else '❌ No'}")
    print(f"Tailwind CDN: {'✅ Yes' if tailwind_ok else '❌ No'}")
    print()
    
    if all_exist and images_exist == len(images) and css_ok and tailwind_ok:
        print("✅ ALL CHECKS PASSED! Website is ready to run.")
        print()
        print("🚀 To start the website, run:")
        print("   python run_website.py")
        return 0
    else:
        print("❌ SOME CHECKS FAILED! Please review the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
