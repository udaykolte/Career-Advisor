// Career & Skills Advisor - JavaScript functionality
document.addEventListener('DOMContentLoaded', function() {
    
    // Multi-step form functionality
    const assessmentForm = document.getElementById('assessmentForm');
    if (assessmentForm) {
        initializeMultiStepForm();
    }
    
    // Initialize animations
    initializeAnimations();
    
    // Initialize skill suggestions
    initializeSkillSuggestions();
    
    // Initialize smooth scrolling
    initializeSmoothScrolling();
    
    // Initialize results animations
    if (document.querySelector('.results-header')) {
        initializeResultsAnimations();
    }
});

// Enhanced Multi-step form functionality
function initializeMultiStepForm() {
    const form = document.getElementById('assessmentForm');
    const steps = document.querySelectorAll('.form-step');
    const progressBar = document.getElementById('progressBar');
    const nextBtns = document.querySelectorAll('.next-btn');
    const prevBtns = document.querySelectorAll('.prev-btn');
    
    let currentStep = 0;
    const totalSteps = steps.length;
    
    // Enhanced progress bar with animation
    function updateProgressBar() {
        const progress = ((currentStep + 1) / totalSteps) * 100;
        
        // Animate progress bar
        progressBar.style.transition = 'width 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
        progressBar.style.width = progress + '%';
        progressBar.setAttribute('aria-valuenow', progress);
        
        // Add color based on progress
        if (progress === 100) {
            progressBar.style.background = 'linear-gradient(135deg, #00b894, #55a3ff)';
        } else {
            progressBar.style.background = 'linear-gradient(135deg, #6c63ff, #4834d4)';
        }
        
        // Show completion celebration
        if (progress === 100) {
            setTimeout(() => {
                showNotification('🎉 Assessment Complete! Ready to get your results!', 'success');
            }, 300);
        }
    }
    
    // Show specific step
    function showStep(stepIndex) {
        steps.forEach((step, index) => {
            step.classList.toggle('active', index === stepIndex);
        });
        updateProgressBar();
        
        // Scroll to form
        document.getElementById('assessment').scrollIntoView({ 
            behavior: 'smooth', 
            block: 'start' 
        });
    }
    
    // Validate current step
    function validateStep(stepIndex) {
        const currentStepElement = steps[stepIndex];
        const requiredFields = currentStepElement.querySelectorAll('[required]');
        let isValid = true;
        
        requiredFields.forEach(field => {
            if (!field.value.trim()) {
                isValid = false;
                field.classList.add('is-invalid');
                
                // Add validation feedback
                const feedback = field.nextElementSibling;
                if (feedback && feedback.classList.contains('invalid-feedback')) {
                    feedback.style.display = 'block';
                }
            } else {
                field.classList.remove('is-invalid');
                field.classList.add('is-valid');
                
                // Hide validation feedback
                const feedback = field.nextElementSibling;
                if (feedback && feedback.classList.contains('invalid-feedback')) {
                    feedback.style.display = 'none';
                }
            }
        });
        
        // Show validation messages with animation
        if (!isValid) {
            currentStepElement.classList.add('shake');
            setTimeout(() => {
                currentStepElement.classList.remove('shake');
            }, 500);
        }
        
        return isValid;
    }
    
    // Next button functionality
    nextBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            
            if (validateStep(currentStep)) {
                if (currentStep < totalSteps - 1) {
                    currentStep++;
                    showStep(currentStep);
                }
            }
        });
    });
    
    // Previous button functionality
    prevBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            
            if (currentStep > 0) {
                currentStep--;
                showStep(currentStep);
            }
        });
    });
    
    // Form submission
    form.addEventListener('submit', function(e) {
        if (!validateStep(currentStep)) {
            e.preventDefault();
            return false;
        }
        
        // Show loading state
        const submitBtn = document.getElementById('submitBtn');
        const originalText = submitBtn.innerHTML;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Analyzing...';
        submitBtn.disabled = true;
        
        // Allow form to submit naturally
        setTimeout(() => {
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
        }, 3000);
    });
    
    // Real-time validation
    const allInputs = form.querySelectorAll('input, select, textarea');
    allInputs.forEach(input => {
        input.addEventListener('input', function() {
            if (this.hasAttribute('required') && this.value.trim()) {
                this.classList.remove('is-invalid');
                this.classList.add('is-valid');
            }
        });
        
        input.addEventListener('blur', function() {
            if (this.hasAttribute('required')) {
                if (!this.value.trim()) {
                    this.classList.add('is-invalid');
                    this.classList.remove('is-valid');
                } else {
                    this.classList.remove('is-invalid');
                    this.classList.add('is-valid');
                }
            }
        });
    });
    
    // Initialize first step
    showStep(0);
}

// Enhanced Skill suggestions functionality
function initializeSkillSuggestions() {
    const skillSuggestions = document.querySelectorAll('.skill-suggestion');
    const skillsTextarea = document.getElementById('skills');
    
    if (!skillsTextarea) return;
    
    skillSuggestions.forEach(suggestion => {
        // Add hover sound effect (optional)
        suggestion.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px) scale(1.05)';
        });
        
        suggestion.addEventListener('mouseleave', function() {
            if (!this.classList.contains('added')) {
                this.style.transform = 'translateY(0) scale(1)';
            }
        });
        
        suggestion.addEventListener('click', function() {
            const skill = this.dataset.skill;
            const currentSkills = skillsTextarea.value;
            
            // Check if skill already exists
            const skillsArray = currentSkills.split(',').map(s => s.trim());
            
            if (!skillsArray.includes(skill)) {
                // Add skill
                const newValue = currentSkills ? `${currentSkills}, ${skill}` : skill;
                skillsTextarea.value = newValue;
                
                // Enhanced visual feedback
                this.classList.add('added');
                this.style.background = 'linear-gradient(135deg, #00b894, #55a3ff)';
                this.style.color = 'white';
                this.style.transform = 'translateY(-3px) scale(1.1)';
                this.style.boxShadow = '0 8px 25px rgba(0,184,148,0.4)';
                
                // Add checkmark
                const checkmark = document.createElement('i');
                checkmark.className = 'fas fa-check ms-1';
                this.appendChild(checkmark);
                
                // Pulse animation
                this.style.animation = 'pulse 0.6s ease-out';
                
                // Show success notification
                showNotification(`✅ Added "${skill}" to your skills!`, 'success');
                
                // Trigger validation
                skillsTextarea.dispatchEvent(new Event('input'));
                
                // Update skill counter
                updateSkillCounter();
            } else {
                // Skill already exists - show feedback
                this.style.animation = 'shake 0.5s ease-out';
                showNotification(`"${skill}" is already in your skills list!`, 'warning');
            }
        });
    });
    
    // Add skill counter
    function updateSkillCounter() {
        const skillCount = skillsTextarea.value.split(',').filter(s => s.trim()).length;
        let counter = document.getElementById('skillCounter');
        if (!counter) {
            counter = document.createElement('small');
            counter.id = 'skillCounter';
            counter.className = 'text-muted mt-2 d-block';
            skillsTextarea.parentNode.appendChild(counter);
        }
        counter.textContent = `${skillCount} skills added`;
        counter.style.color = skillCount > 0 ? '#00b894' : '#636e72';
    }
    
    // Initialize counter
    updateSkillCounter();
    
    // Update counter on manual input
    skillsTextarea.addEventListener('input', updateSkillCounter);
}

// Animation initialization
function initializeAnimations() {
    // Fade in elements on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animateElements = document.querySelectorAll('.feature-card, .step-number, .profile-stat, .career-card');
    animateElements.forEach(el => observer.observe(el));
    
    // Counter animation for stats
    const statNumbers = document.querySelectorAll('.stat-item h3');
    statNumbers.forEach(stat => {
        const finalValue = parseInt(stat.textContent);
        if (!isNaN(finalValue)) {
            animateCounter(stat, 0, finalValue, 2000);
        }
    });
}

// Counter animation
function animateCounter(element, start, end, duration) {
    const range = end - start;
    const increment = range / (duration / 16); // 60fps
    let current = start;
    
    const timer = setInterval(() => {
        current += increment;
        if (current >= end) {
            current = end;
            clearInterval(timer);
        }
        element.textContent = Math.floor(current) + (element.textContent.includes('+') ? '+' : '');
    }, 16);
}

// Smooth scrolling for anchor links
function initializeSmoothScrolling() {
    const scrollLinks = document.querySelectorAll('a[href^="#"]');
    
    scrollLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Results page animations
function initializeResultsAnimations() {
    // Animate progress bars
    setTimeout(() => {
        const progressBars = document.querySelectorAll('.skill-progress .progress-bar');
        progressBars.forEach((bar, index) => {
            setTimeout(() => {
                bar.style.width = bar.style.width || '0%';
            }, index * 200);
        });
    }, 500);
    
    // Animate timeline items
    const timelineItems = document.querySelectorAll('.timeline-item');
    timelineItems.forEach((item, index) => {
        setTimeout(() => {
            item.classList.add('animate-slide-in');
        }, index * 300);
    });
    
    // Typewriter effect for motivation text
    const motivationText = document.querySelector('.motivation-content p');
    if (motivationText) {
        const text = motivationText.textContent;
        motivationText.textContent = '';
        motivationText.style.borderRight = '2px solid #007bff';
        
        let i = 0;
        const typeWriter = () => {
            if (i < text.length) {
                motivationText.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 50);
            } else {
                motivationText.style.borderRight = 'none';
            }
        };
        
        setTimeout(typeWriter, 1000);
    }
}

// Utility functions
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} notification-toast`;
    notification.innerHTML = `
        <i class="fas fa-info-circle me-2"></i>
        ${message}
        <button type="button" class="btn-close ms-auto" onclick="this.parentElement.remove()"></button>
    `;
    
    // Add styles
    notification.style.position = 'fixed';
    notification.style.top = '20px';
    notification.style.right = '20px';
    notification.style.zIndex = '9999';
    notification.style.minWidth = '300px';
    notification.style.animation = 'slideInRight 0.5s ease';
    
    document.body.appendChild(notification);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (notification.parentElement) {
            notification.style.animation = 'slideOutRight 0.5s ease';
            setTimeout(() => notification.remove(), 500);
        }
    }, 5000);
}

// Form validation helpers
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validatePhone(phone) {
    const re = /^[\+]?[1-9][\d]{0,15}$/;
    return re.test(phone.replace(/\s+/g, ''));
}

// Local storage helpers
function saveFormProgress(formData) {
    localStorage.setItem('career_advisor_progress', JSON.stringify(formData));
}

function loadFormProgress() {
    const saved = localStorage.getItem('career_advisor_progress');
    return saved ? JSON.parse(saved) : null;
}

function clearFormProgress() {
    localStorage.removeItem('career_advisor_progress');
}

// Enhanced CSS animations and styles
const style = document.createElement('style');
style.textContent = `
    .animate-fade-in {
        animation: fadeInUp 0.8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(40px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .animate-slide-in {
        animation: slideInLeft 0.6s cubic-bezier(0.4, 0, 0.2, 1) forwards;
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-40px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
    
    .shake {
        animation: shake 0.5s ease-in-out;
    }
    
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        10%, 30%, 50%, 70%, 90% { transform: translateX(-8px); }
        20%, 40%, 60%, 80% { transform: translateX(8px); }
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.15); }
        100% { transform: scale(1.1); }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 5px rgba(108, 99, 255, 0.5); }
        50% { box-shadow: 0 0 20px rgba(108, 99, 255, 0.8), 0 0 30px rgba(108, 99, 255, 0.6); }
    }
    
    .form-step {
        opacity: 0;
        transform: translateX(20px);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .form-step.active {
        opacity: 1;
        transform: translateX(0);
    }
    
    .notification-toast {
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        border: none;
        border-radius: 12px;
        backdrop-filter: blur(10px);
        border-left: 4px solid;
    }
    
    .notification-toast.alert-success {
        background: rgba(0, 184, 148, 0.95);
        border-left-color: #00b894;
        color: white;
    }
    
    .notification-toast.alert-warning {
        background: rgba(253, 203, 110, 0.95);
        border-left-color: #fdcb6e;
        color: #2d3436;
    }
    
    .notification-toast.alert-info {
        background: rgba(0, 206, 201, 0.95);
        border-left-color: #00cec9;
        color: white;
    }
    
    /* Enhanced hover effects */
    .btn:hover {
        animation: glow 1.5s ease-in-out infinite alternate;
    }
    
    .career-card:hover {
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    .profile-stat:hover {
        animation: glow 1.5s ease-in-out infinite alternate;
    }
`;

document.head.appendChild(style);

// Error handling
window.addEventListener('error', function(e) {
    console.error('Application error:', e.error);
    showNotification('An unexpected error occurred. Please try again.', 'danger');
});

// Performance monitoring
if ('performance' in window) {
    window.addEventListener('load', function() {
        setTimeout(function() {
            const perfData = performance.timing;
            const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
            console.log(`Page loaded in ${pageLoadTime}ms`);
        }, 0);
    });
}