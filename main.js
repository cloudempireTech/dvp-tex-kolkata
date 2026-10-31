// DVP Tex Kolkata - Main JS Engine

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Drawer Toggle
  const toggleBtn = document.querySelector('.mobile-nav-toggle');
  const drawer = document.querySelector('.mobile-nav-drawer');

  if (toggleBtn && drawer) {
    toggleBtn.addEventListener('click', () => {
      drawer.classList.toggle('open');
    });

    document.addEventListener('click', (e) => {
      if (!drawer.contains(e.target) && !toggleBtn.contains(e.target) && drawer.classList.contains('open')) {
        drawer.classList.remove('open');
      }
    });
  }

  // 2. Dynamic Typewriter Headline
  const typeTarget = document.querySelector('.typewriter-target');
  if (typeTarget) {
    const phrases = [
      "Export Textile Bags",
      "Home & Hospitality Made-Ups",
      "Heavy Duck & Twill Fabrics",
      "Global OEM/ODM Solutions",
      "Azo-Free Certified Quality"
    ];

    let phraseIdx = 0;
    let charIdx = 0;
    let isDeleting = false;
    let typeSpeed = 100;

    function typeLoop() {
      const current = phrases[phraseIdx];

      if (isDeleting) {
        typeTarget.textContent = current.substring(0, charIdx - 1);
        charIdx--;
        typeSpeed = 45;
      } else {
        typeTarget.textContent = current.substring(0, charIdx + 1);
        charIdx++;
        typeSpeed = 90;
      }

      if (!isDeleting && charIdx === current.length) {
        isDeleting = true;
        typeSpeed = 1800; // Pause before deleting
      } else if (isDeleting && charIdx === 0) {
        isDeleting = false;
        phraseIdx = (phraseIdx + 1) % phrases.length;
        typeSpeed = 400; // Pause before next word
      }

      setTimeout(typeLoop, typeSpeed);
    }

    typeLoop();
  }

  // 3. Counter Animation on Scroll
  const counters = document.querySelectorAll('.counter-val');
  let countersAnimated = false;

  function runCounters() {
    if (countersAnimated) return;
    counters.forEach(counter => {
      const target = +counter.getAttribute('data-target');
      const duration = 1600;
      const stepTime = 20;
      const steps = duration / stepTime;
      const increment = target / steps;
      let current = 0;

      const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
          counter.textContent = target;
          clearInterval(timer);
        } else {
          counter.textContent = Math.floor(current);
        }
      }, stepTime);
    });
    countersAnimated = true;
  }

  const counterBar = document.querySelector('.counter-bar-wrapper');
  if (counterBar) {
    const observer = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting) {
        runCounters();
      }
    }, { threshold: 0.2 });
    observer.observe(counterBar);
  }

  // 4. Interactive Export RFQ & Specification Intake Widget
  const rfqCategory = document.getElementById('rfqCategory');
  const rfqMaterial = document.getElementById('rfqMaterial');
  const rfqVolume = document.getElementById('rfqVolume');
  const rfqDestination = document.getElementById('rfqDestination');
  const rfqDetails = document.getElementById('rfqDetails');
  const rfqWaBtn = document.getElementById('rfqWaBtn');

  function updateRfq() {
    if (!rfqCategory || !rfqMaterial || !rfqVolume || !rfqDestination || !rfqDetails || !rfqWaBtn) return;

    const cat = rfqCategory.value;
    const mat = rfqMaterial.value;
    const vol = rfqVolume.value;
    const dest = rfqDestination.value;

    let specs = "";
    if (cat.includes("Bags")) {
      specs = `Reinforced handles, custom screen/rotary print, AZO-free dye, standard export carton packaging.`;
    } else if (cat.includes("Made-Ups")) {
      specs = `Pre-shrunk, mercerized finish, hemstitched borders, barcode retail ready tagging.`;
    } else {
      specs = `Custom width 58" - 72", continuous loom rolls, shrink-wrapped with moisture barrier.`;
    }

    rfqDetails.innerHTML = `<strong>Selected Program:</strong> ${cat} (${mat})<br><span style="color: #94a3b8; font-size: 0.88rem;"><strong>Export Specifications:</strong> ${specs} | Target Volume: ${vol} | Destination: ${dest}</span>`;

    const msg = `Hello DVP Tex Export Team! We would like to request an official RFQ & spec sheet for ${cat} (${mat}). Volume: ${vol}, Destination: ${dest}. Please share technical lead times.`;
    rfqWaBtn.href = `https://wa.me/919007577861?text=${encodeURIComponent(msg)}`;
  }

  if (rfqCategory) {
    rfqCategory.addEventListener('change', updateRfq);
    rfqMaterial.addEventListener('change', updateRfq);
    rfqVolume.addEventListener('change', updateRfq);
    rfqDestination.addEventListener('change', updateRfq);
    updateRfq();
  }
});
