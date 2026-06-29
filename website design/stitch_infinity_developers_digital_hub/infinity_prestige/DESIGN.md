---
name: Infinity Prestige
colors:
  surface: '#fff8f0'
  surface-dim: '#e1d9cc'
  surface-bright: '#fff8f0'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fbf3e5'
  surface-container: '#f5eddf'
  surface-container-high: '#efe7da'
  surface-container-highest: '#eae1d4'
  on-surface: '#1f1b13'
  on-surface-variant: '#4d4635'
  inverse-surface: '#343027'
  inverse-on-surface: '#f8f0e2'
  outline: '#7f7663'
  outline-variant: '#d0c5af'
  surface-tint: '#735c00'
  primary: '#735c00'
  on-primary: '#ffffff'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#e9c349'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e2dfde'
  on-secondary-container: '#636262'
  tertiary: '#415ba4'
  on-tertiary: '#ffffff'
  tertiary-container: '#97b0ff'
  on-tertiary-container: '#254188'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#dbe1ff'
  tertiary-fixed-dim: '#b4c5ff'
  on-tertiary-fixed: '#00174b'
  on-tertiary-fixed-variant: '#27438a'
  background: '#fff8f0'
  on-background: '#1f1b13'
  surface-variant: '#eae1d4'
  bronze-deep: '#8C6A1C'
  charcoal-black: '#0D0D0D'
  surface-ivory: '#F9F9F7'
  border-muted: '#E5E5E1'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  container-max: 1280px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  section-gap: 120px
---

## Brand & Style

This design system embodies the "Your Aspiration, Your World" motto by merging high-end architectural aesthetics with institutional reliability. The brand personality is **Sophisticated, Professional, and Established**. It targets high-net-worth investors and aspirational homebuyers who value precision and legacy.

The visual style is **Corporate / Modern with Minimalist influences**. It leverages generous whitespace, a rigid grid structure, and a "Glass Facade" philosophy—prioritizing transparency, crisp edges, and reflective surfaces. The interface should feel like a walkthrough of a premium gallery: quiet, expensive, and intentional.

## Colors

The palette is anchored by **Metallic Gold (#D4AF37)**, used as a strategic accent to denote premium status and primary actions. **Charcoal Black** provides the structural weight, used for primary typography and high-contrast UI elements.

Backgrounds utilize **Surface Ivory** and pure white to maintain a "clean" feel that avoids the starkness of clinical gray. Use the deeper **Bronze** for hover states or gradients to simulate light hitting a metallic surface. Text contrast must remain high to ensure readability of technical real estate specifications.

## Typography

The system employs a dual-font strategy:
- **Playfair Display**: Used for headlines and display text. Its high-contrast serifs evoke a sense of heritage and luxury.
- **Manrope**: A modern, geometric sans-serif used for body copy and technical data. It ensures maximum legibility for RERA numbers, area calculations, and contact details.

**Styling Note**: Use `label-caps` for categorical labeling (e.g., "LOCATION & CONNECTIVITY") to provide a clear structural anchor for sections.

## Layout & Spacing

The design system uses a **Fixed Grid** model for desktop, centered within a maximum width of 1280px. A 12-column system provides the structure for property listings and amenity grids.

**Rhythm**:
- **Section Gaps**: Use a generous 120px vertical margin between major narrative blocks (e.g., from "Hero" to "Amenities") to allow the design to "breathe."
- **Internal Padding**: Components like project cards use a 32px inner padding to maintain an airy, premium feel.
- **Mobile Adaption**: Margins shrink to 20px, and section gaps reduce to 64px. Multi-column grids reflow to a single stack, prioritizing vertical imagery.

## Elevation & Depth

Visual hierarchy is established through **Tonal Layers** and **Ambient Shadows**:
- **Base Level**: Pure white or Surface Ivory background.
- **Card Level**: Subtle, extra-diffused shadows (`0 4px 20px rgba(0,0,0,0.05)`) simulate physical paper or architectural models resting on a surface.
- **Interactive Layer**: Floating Enquiry buttons and "Call Now" triggers use a higher Z-index with a slightly more pronounced shadow to indicate they sit above the content.
- **Glassmorphism**: Modals and navigation bars should utilize a backdrop blur (12px) with a semi-transparent white tint (80% opacity) to mimic the "Glass Facade" of the buildings.

## Shapes

The shape language is **Soft (0.25rem)**. While the overall architectural vibe is sharp and precise, subtle rounding on buttons and cards prevents the UI from feeling aggressive. 

Large-scale containers, such as hero images and "Master Plan" sections, should remain **Sharp (0px)** to reflect the structural integrity of real estate development. Icons should follow a thin-stroke (1.5px) linear style to match the elegance of the typography.

## Components

### Buttons
- **Primary**: Solid Gold (#D4AF37) with white text. High-contrast, rectangular with minimal rounding.
- **Secondary**: Charcoal Black border (1px) with black text. 
- **CTA**: Persistent "Call Now" or "Enquiry" buttons use a gold-to-bronze subtle gradient to draw the eye.

### Project Cards
- Use a white background with a subtle ambient shadow. 
- Images should occupy the top 60% of the card.
- Text content should be aligned left with generous 32px padding.

### Input Fields
- Underlined style or very light borders (#E5E5E1).
- Focus state should transition the border color to Gold.
- Use `label-caps` for field headers.

### Amenities & Chips
- Use consistent, thin-line gold icons.
- Labels in Manrope Medium 14px.
- Chips for "On-Going" or "Ready to Move" should use a charcoal background with white all-caps text for high-impact status tracking.

### Modals (Enquiry)
- Full-screen or large center-aligned overlays with a heavy backdrop blur.
- Close button ("×") should be prominent in the top right.