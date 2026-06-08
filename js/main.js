(function() {
  'use strict';

  function initScrollReveal() {
    var reveals = document.querySelectorAll('.fade-in');
    if (!reveals.length) return;

    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -40px 0px'
    });

    reveals.forEach(function(el) {
      observer.observe(el);
    });
  }

  function initMobileMenu() {
    var menuBtn = document.getElementById('mobileMenuBtn');
    var closeBtn = document.getElementById('closeDrawerBtn');
    var drawer = document.getElementById('mobileDrawer');

    if (!menuBtn || !drawer) return;

    function openDrawer() {
      drawer.classList.remove('translate-x-full');
      document.body.style.overflow = 'hidden';
    }

    function closeDrawer() {
      drawer.classList.add('translate-x-full');
      document.body.style.overflow = '';
    }

    menuBtn.addEventListener('click', openDrawer);
    if (closeBtn) closeBtn.addEventListener('click', closeDrawer);

    drawer.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', closeDrawer);
    });
  }

  function initFAQ() {
    var toggles = document.querySelectorAll('.faq-toggle');
    toggles.forEach(function(toggle) {
      toggle.addEventListener('click', function() {
        var content = this.nextElementSibling;
        var icon = this.querySelector('.faq-icon');
        var isOpen = content.style.maxHeight && content.style.maxHeight !== '0px';

        toggles.forEach(function(t) {
          t.nextElementSibling.style.maxHeight = '0px';
          var ic = t.querySelector('.faq-icon');
          if (ic) ic.style.transform = 'rotate(0deg)';
        });

        if (!isOpen) {
          content.style.maxHeight = content.scrollHeight + 'px';
          if (icon) icon.style.transform = 'rotate(180deg)';
        }
      });
    });
  }

  function initContactForm() {
    var form = document.getElementById('contactForm');
    if (!form) return;

    form.addEventListener('submit', function(e) {
      e.preventDefault();
      var btn = form.querySelector('button[type="submit"]');
      var originalText = btn.textContent;
      btn.textContent = 'Sending...';
      btn.disabled = true;
      btn.style.opacity = '0.7';

      setTimeout(function() {
        btn.textContent = 'Message Sent!';
        btn.style.opacity = '1';
        btn.style.background = 'var(--color-tertiary-container)';

        setTimeout(function() {
          btn.textContent = originalText;
          btn.style.background = '';
          btn.disabled = false;
          form.reset();
        }, 2500);
      }, 1200);
    });
  }

  document.addEventListener('DOMContentLoaded', function() {
    initScrollReveal();
    initMobileMenu();
    initFAQ();
    initContactForm();
  });
})();
