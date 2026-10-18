# Mathematical Modeling of Nanoporous Filtration: A Computational Framework Towards Bioartificial Organs

> **Author:** Sathya Jothi | B.E. Mechanical Engineering  
> **Academic Goal:** MSc Mathematical Modelling and Computational Sciences (University of Luxembourg) → PhD in Computational Science & Engineering (ETH Zurich / Ivy League)

## 🎯 Research Vision
To develop a robust, open-source computational framework for modeling transport phenomena in nanoporous membranes, bridging **Applied Mathematics, Computational Fluid Dynamics (CFD), and Biomechanical Systems**. This project is a first step towards my long-term goal: **contributing to implantable bioartificial organs through advanced mathematical modeling**, targeting doctoral research at **ETH Zurich, MIT, Stanford, or equivalent**.

## 🔬 Problem Statement
How does nanoscale pore geometry affect pressure-driven filtration efficiency in silicon membranes for implantable hemofiltration?

This requires solving coupled fluid dynamics at low Reynolds numbers, where classical continuum assumptions need geometric corrections.

## ⚙️ Mathematical Formulation

**1. Governing Physics: Stokes Flow Regime (Re << 1)**
For nanopores, inertial terms are negligible. We use Hagen-Poiseuille derived from Navier-Stokes:
$$ \nabla p = \mu \nabla^2 \mathbf{u} $$

**2. Reduced Order Model for Parametric Study:**
$$ Q(\Delta P, G) = \frac{\Delta P}{R_{hyd}(G)} $$
Where hydraulic resistance $R_{hyd}$ is a function of geometry $G$:

- **Circular:** $R_{hyd} = \frac{8 \mu L}{\pi r^4} \cdot \frac{1}{n}$
- **Slit (Rectangular):** $R_{hyd} = \frac{12 \mu L}{w h^3 [1 - 0.63(h/w)]} \cdot \frac{1}{n}$ (for h < w)

**3. Non-dimensional Analysis:**
Computed normalized flow $Q^* = Q_{slit}/Q_{circular}$ to isolate geometric effect.

## 📊 Computational Result & Key Insight
![Filtration Comparison](filtration_comparision.png.png)

**Finding:** Slit-pore architecture yields **15-18% higher volumetric throughput** across physiological MAP (80-180 mmHg). This aligns with literature from The Kidney Project (UCSF, Roy et al.) and provides a mathematically rigorous basis for geometry optimization.

> Code reproducibility: Simulation performed in Python (NumPy/Matplotlib) with vectorized parametric sweep.

## 💻 Computational Methods & Skills
This project demonstrates core competencies for MSc MMCS and future PhD:

- **Applied Mathematics:** PDE formulation, Dimensional Analysis, Lubrication Theory
- **Numerical Methods:** Parametric discretization, Convergence analysis, Vectorized computing
- **Scientific Computing:** Python, NumPy, Matplotlib, Git/GitHub, Google Colab
- **Fluid Mechanics:** Viscous flow, Microfluidics, Porous media transport
- **Engineering Background:** B.E. Mechanical - Strong foundation in FM, Thermodynamics, Numerical Methods

## 🚀 Roadmap to PhD (ETH Zurich / Ivy League Focus)

**Phase 1 (Current - Luxembourg MSc):** 
- Validate reduced model with high-fidelity solvers (FEniCS / OpenFOAM)
- Incorporate non-Newtonian rheology (Carreau-Yasuda) and particle transport (convection-diffusion PDE)

**Phase 2 (MSc Thesis):**
- Coupled fluid-structure interaction (FSI) of silicon membrane under pulsatile flow
- Uncertainty Quantification (UQ) & Sensitivity Analysis for fouling and long-term reliability

**Phase 3 (PhD Goal):**
- Develop full-scale computational model of implantable bioartificial kidney (hemofilter + bioreactor)
- Multi-scale modeling (molecular dynamics → continuum) for membrane-protein interaction
- Aim for publication in *Journal of Computational Physics* / *Lab on a Chip*

This aligns directly with research groups at **CSElab, Harvard SEAS (Prof. Koumoutsakos), MIT (MechE - Biofluids), Stanford (Institute for Computational & Mathematical Engineering)**.

## 📚 References
1. Fissell, W.H., Dubnisheva, A., Eldridge, A.N., et al., *High-Performance Silicon Nanopore Hemofiltration Membranes*, Journal of Membrane Science, 326, 58-63 (2009).
2. Kensinger, C., et al., *First Implantation of Silicon Nanopore Membrane Hemofilters*, ASAIO Journal, 62, 491-495 (2016).
3. Bruus, H., *Theoretical Microfluidics*, Oxford University Press (2008).
4. Roy, S., Fissell, W.H., et al., *The Kidney Project, UCSF - Implantable Bioartificial Kidney*, Nature Communications (2023) & Annual Reviews.

## 📫 Contact & Portfolio
**Sathya Jothi** | B.E. Mechanical Engineering | Aspiring Computational Scientist
- Email: sathyajothi83@gmail.com
- GitHub: @sathya-guru
- Focus: Mathematical Modeling, CFD, Scientific ML

---
*This repository is part of my academic portfolio for MSc Mathematical Modelling and Computational Sciences, University of Luxembourg, with a clear trajectory towards doctoral research in Computational Science & Engineering at ETH Zurich / Ivy League institutions.*
