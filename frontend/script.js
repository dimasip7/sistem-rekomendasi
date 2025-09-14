let currentStep = 0;
const steps = document.querySelectorAll(".form-step");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");

showStep(currentStep);

function showStep(n) {
  steps.forEach((step, index) => {
    step.classList.toggle("active", index === n);
  });

  prevBtn.style.display = n === 0 ? "none" : "inline-block";
  nextBtn.innerText = (n === steps.length - 1) ? "Submit" : "Next";
}

nextBtn.addEventListener("click", () => {
  if (currentStep < steps.length - 1) {
    currentStep++;
    showStep(currentStep);
  } else {
    alert("Form selesai, rekomendasi ditampilkan di bawah 🎉");
  }
});

prevBtn.addEventListener("click", () => {
  if (currentStep > 0) {
    currentStep--;
    showStep(currentStep);
  }
});