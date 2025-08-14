# AccessAble

AccessAble is a project dedicated to showcasing current accessibility tools available for web users. Its goal is to raise awareness and provide resources for making the web more inclusive for everyone, including people with disabilities.

## Project Structure

```
AccessAble/
├── index.html              # Main landing page
├── web-accessibility-tools.html  # Tools and resources page
├── static/
│   └── styles.css         # Accessible stylesheet
├── generate_nav.py        # Navigation generator script
└── README.md
```

## What is Accessibility?

Web accessibility refers to the practice of designing and developing websites, applications, and digital tools so that people with disabilities can perceive, understand, navigate, and interact with them effectively. This includes people with various disabilities such as:

- **Visual impairments**: Blindness, low vision, color blindness
- **Hearing impairments**: Deafness or hearing loss
- **Motor impairments**: Limited fine motor control, paralysis
- **Cognitive impairments**: Learning disabilities, memory issues, attention disorders

Accessibility benefits everyone, not just people with disabilities. Features like captions, keyboard navigation, and clear design improve the user experience for all users.

## Why is Web Accessibility Important?

Web accessibility is crucial for several reasons:

- **Legal compliance**: Many countries have laws requiring digital accessibility (e.g., ADA in the US, AODA in Canada, EN 301 549 in the EU)
- **Inclusive design**: Ensures equal access to information and functionality for all users
- **Business benefits**: Expands your potential audience and customer base
- **Better user experience**: Accessibility improvements often enhance usability for everyone
- **Social responsibility**: Promotes digital equity and inclusion in our increasingly digital world
- **SEO benefits**: Many accessibility practices also improve search engine optimization

## Purpose

The purpose of this project is to:

- Highlight and demonstrate modern accessibility tools and features for web users
- Educate developers and users about best practices in web accessibility
- Provide examples and resources to help improve web accessibility

## Features

- Overview of popular accessibility tools (screen readers, browser extensions, etc.)
- Demos and guides for using accessibility features
- Resources for learning more about web accessibility
- Semantic HTML structure with ARIA roles and skip links for improved accessibility
- Responsive design and color contrast for better usability
- Automatic navigation generation across pages
- Dark mode support and color scheme preferences
- High contrast mode support

## Technical Features

### Automated Navigation
- Python script (`generate_nav.py`) automatically generates navigation menus
- Detects all HTML pages in the project
- Updates navigation with proper ARIA attributes
- Maintains current page indicators

### CSS Features
- CSS Custom Properties (variables) for easy theming
- Responsive design with mobile-first approach
- High contrast mode support
- Focus visible indicators
- Smooth scrolling
- Accessible color contrast ratios
- Dark mode support

### Testing

The site has been tested with:
- WAVE Web Accessibility Evaluation Tool
- axe DevTools
- Keyboard navigation
- Various screen readers (NVDA, VoiceOver)
- High contrast mode
- Different viewport sizes

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/nikolmichaelidou/AccessAble.git
   cd AccessAble
   ```

2. Update the navigation (optional):
   ```bash
   python3 generate_nav.py
   ```
   This will automatically update the navigation menu across all HTML pages.

3. Start a local server:
   ```bash
   python3 -m http.server 8000
   ```

4. Open `http://localhost:8000` in your browser to explore the site.

## Accessibility Best Practices Used

- Semantic HTML elements (`<header>`, `<nav>`, `<main>`, `<footer>`, etc.)
- ARIA roles and labels for navigation and landmarks
- Skip navigation links for screen readers
- Descriptive link text and `aria-label` attributes
- Responsive meta tags and color scheme support
- Sufficient color contrast and accessible font sizes
- All interactive elements are keyboard accessible

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Run `python3 generate_nav.py` to update navigation if you've added pages
5. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
6. Push to the branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

## License

This project is open source and available under the MIT License.
