# Citera eval v2: label review

Questions were drafted by an LLM from one abstract each; nothing below is pre-ticked except the gold paper.

**How to review**
- Tick a candidate by changing `[ ]` to `[x]` if that paper's abstract helps answer the question.
- The gold paper is already ticked; untick it if the question does not really match it.
- You may edit the text after `**Question:**`.
- To drop a question, delete its whole section or change its heading to `## Q07 DELETE`.
- Do not change the paper ids in backticks; the parser relies on them.
- Candidates are in paper-id order, not rank order.

## Q01

**Question:** How can changing the loss used at training time make a conditional diffusion model less sensitive to the guidance strength chosen at sampling time?

**Gold:** `2311.00938v1` | Bridging the Gap: Addressing Discrepancies in Diffusion Model Training for Classifier-Free Guidance

> Diffusion models have emerged as a pivotal advancement in generative models, setting new standards to the quality of the generated instances. In the current paper we aim to underscore a discrepancy between conventional training methods and the desired conditional sampling behavior of these models.

**Candidates:**

- [ ] relevant | `2207.12598v1` | Classifier-Free Diffusion Guidance | Classifier guidance is a recently introduced method to trade off mode coverage and sample fidelity in conditional diffusion models post training, in the same spirit as low temperature sampling or truncation in other types of generative models.
- [x] relevant (gold) | `2311.00938v1` | Bridging the Gap: Addressing Discrepancies in Diffusion Model Training for Classifier-Free Guidance | Diffusion models have emerged as a pivotal advancement in generative models, setting new standards to the quality of the generated instances.
- [ ] relevant | `2312.02246v4` | Conditional Variational Diffusion Models | Inverse problems aim to determine parameters from observations, a crucial task in engineering and science.
- [ ] relevant | `2312.07586v5` | Characteristic Guidance: Non-linear Correction for Diffusion Model at Large Guidance Scale | Popular guidance for denoising diffusion probabilistic model (DDPM) linearly combines distinct conditional models together to provide enhanced control over samples.
- [ ] relevant | `2404.07724v2` | Applying Guidance in a Limited Interval Improves Sample and Distribution Quality in Diffusion Models | Guidance is a crucial technique for extracting the best performance out of image-generating diffusion models.
- [ ] relevant | `2406.17399v1` | GradCheck: Analyzing classifier guidance gradients for conditional diffusion sampling | To sample from an unconditionally trained Denoising Diffusion Probabilistic Model (DDPM), classifier guidance adds conditional information during sampling, but the gradients from classifiers, especially those not trained on noisy images, are often unstable.
- [ ] relevant | `2407.02687v2` | No Training, No Problem: Rethinking Classifier-Free Guidance for Diffusion Models | Classifier-free guidance (CFG) has become the standard method for enhancing the quality of conditional diffusion models.
- [ ] relevant | `2412.09966v1` | EP-CFG: Energy-Preserving Classifier-Free Guidance | Classifier-free guidance (CFG) is widely used in diffusion models but often introduces over-contrast and over-saturation artifacts at higher guidance strengths.
- [ ] relevant | `2505.21101v1` | Conditional Diffusion Models with Classifier-Free Gibbs-like Guidance | Classifier-Free Guidance (CFG) is a widely used technique for improving conditional diffusion models by linearly combining the outputs of conditional and unconditional denoisers.
- [ ] relevant | `2506.10036v2` | Token Perturbation Guidance for Diffusion Models | Classifier-free guidance (CFG) has become an essential component of modern diffusion models to enhance both generation quality and alignment with input conditions.
- [ ] relevant | `2507.08965v2` | Improving Classifier-Free Guidance in Masked Diffusion: Low-Dim Theoretical Insights with High-Dim Impact | Classifier-Free Guidance (CFG) is a widely used technique for conditional generation and improving sample quality in continuous diffusion models, and its extensions to discrete diffusion has recently started to be investigated.
- [ ] relevant | `2509.22007v2` | Stage-wise Dynamics of Classifier-Free Guidance in Diffusion Models | Classifier-Free Guidance (CFG) is widely used to improve conditional fidelity in diffusion models, but its impact on sampling dynamics remains poorly understood.
- [ ] relevant | `2511.05844v3` | Enhancing Diffusion Model Guidance through Calibration and Regularization | Classifier-guided diffusion models have emerged as a powerful approach for conditional image generation, but they suffer from overconfident predictions during early denoising steps, causing the guidance gradient to vanish.
- [ ] relevant | `2512.17303v1` | EMAG: Self-Rectifying Diffusion Sampling with Exponential Moving Average Guidance | In diffusion and flow-matching generative models, guidance techniques are widely used to improve sample quality and consistency.
- [ ] relevant | `2603.08155v3` | C$^2$FG: Control Classifier-Free Guidance via Score Discrepancy Analysis | Classifier-Free Guidance (CFG) is a cornerstone of modern conditional diffusion models, yet its reliance on the fixed or heuristic dynamic guidance weight is predominantly empirical and overlooks the inherent dynamics of the diffusion process.

## Q02

**Question:** Can a diffusion model be trained so that it no longer has to combine conditional and unconditional predictions at inference, and what does that do to inference speed?

**Gold:** `2502.12154v1` | Diffusion Models without Classifier-free Guidance

> This paper presents Model-guidance (MG), a novel objective for training diffusion model that addresses and removes of the commonly used Classifier-free guidance (CFG). Our innovative approach transcends the standard modeling of solely data distribution to incorporating the posterior probability of conditions.

**Candidates:**

- [ ] relevant | `2207.12598v1` | Classifier-Free Diffusion Guidance | Classifier guidance is a recently introduced method to trade off mode coverage and sample fidelity in conditional diffusion models post training, in the same spirit as low temperature sampling or truncation in other types of generative models.
- [ ] relevant | `2310.05264v5` | The Emergence of Reproducibility and Generalizability in Diffusion Models | In this work, we investigate an intriguing and prevalent phenomenon of diffusion models which we term as "consistent model reproducibility": given the same starting noise input and a deterministic sampler, different diffusion models often yield remarkably similar outputs.
- [ ] relevant | `2311.00938v1` | Bridging the Gap: Addressing Discrepancies in Diffusion Model Training for Classifier-Free Guidance | Diffusion models have emerged as a pivotal advancement in generative models, setting new standards to the quality of the generated instances.
- [ ] relevant | `2312.02246v4` | Conditional Variational Diffusion Models | Inverse problems aim to determine parameters from observations, a crucial task in engineering and science.
- [ ] relevant | `2312.07586v5` | Characteristic Guidance: Non-linear Correction for Diffusion Model at Large Guidance Scale | Popular guidance for denoising diffusion probabilistic model (DDPM) linearly combines distinct conditional models together to provide enhanced control over samples.
- [ ] relevant | `2402.05098v4` | Improved off-policy training of diffusion samplers | We study the problem of training diffusion models to sample from a distribution with a given unnormalized density or energy function.
- [ ] relevant | `2407.01392v4` | Diffusion Forcing: Next-token Prediction Meets Full-Sequence Diffusion | This paper presents Diffusion Forcing, a new training paradigm where a diffusion model is trained to denoise a set of tokens with independent per-token noise levels.
- [ ] relevant | `2407.02687v2` | No Training, No Problem: Rethinking Classifier-Free Guidance for Diffusion Models | Classifier-free guidance (CFG) has become the standard method for enhancing the quality of conditional diffusion models.
- [x] relevant (gold) | `2502.12154v1` | Diffusion Models without Classifier-free Guidance | This paper presents Model-guidance (MG), a novel objective for training diffusion model that addresses and removes of the commonly used Classifier-free guidance (CFG).
- [ ] relevant | `2503.10638v3` | Studying Classifier(-Free) Guidance From a Classifier-Centric Perspective | Classifier-free guidance has become a staple for conditional generation with denoising diffusion models.
- [ ] relevant | `2505.21101v1` | Conditional Diffusion Models with Classifier-Free Gibbs-like Guidance | Classifier-Free Guidance (CFG) is a widely used technique for improving conditional diffusion models by linearly combining the outputs of conditional and unconditional denoisers.
- [ ] relevant | `2506.10036v2` | Token Perturbation Guidance for Diffusion Models | Classifier-free guidance (CFG) has become an essential component of modern diffusion models to enhance both generation quality and alignment with input conditions.
- [ ] relevant | `2507.05914v3` | Accelerating Diffusion Model Training under Minimal Budgets: A Condensation-Based Perspective | Diffusion models have achieved remarkable performance on a wide range of generative tasks, yet training them from scratch is notoriously resource-intensive, typically requiring millions of training images and many GPU days.
- [ ] relevant | `2603.08155v3` | C$^2$FG: Control Classifier-Free Guidance via Score Discrepancy Analysis | Classifier-Free Guidance (CFG) is a cornerstone of modern conditional diffusion models, yet its reliance on the fixed or heuristic dynamic guidance weight is predominantly empirical and overlooks the inherent dynamics of the diffusion process.

## Q03

**Question:** When the conditional distribution has several modes, what successive phases does guided sampling go through, and why does stronger guidance reduce diversity?

**Gold:** `2509.22007v2` | Stage-wise Dynamics of Classifier-Free Guidance in Diffusion Models

> Classifier-Free Guidance (CFG) is widely used to improve conditional fidelity in diffusion models, but its impact on sampling dynamics remains poorly understood. Prior studies, often restricted to unimodal conditional distributions or simplified cases, provide only a partial picture.

**Candidates:**

- [ ] relevant | `2207.12598v1` | Classifier-Free Diffusion Guidance | Classifier guidance is a recently introduced method to trade off mode coverage and sample fidelity in conditional diffusion models post training, in the same spirit as low temperature sampling or truncation in other types of generative models.
- [ ] relevant | `2301.11558v1` | Accelerating Guided Diffusion Sampling with Splitting Numerical Methods | Guided diffusion is a technique for conditioning the output of a diffusion model at sampling time without retraining the network for each specific task.
- [ ] relevant | `2311.00938v1` | Bridging the Gap: Addressing Discrepancies in Diffusion Model Training for Classifier-Free Guidance | Diffusion models have emerged as a pivotal advancement in generative models, setting new standards to the quality of the generated instances.
- [ ] relevant | `2312.07586v5` | Characteristic Guidance: Non-linear Correction for Diffusion Model at Large Guidance Scale | Popular guidance for denoising diffusion probabilistic model (DDPM) linearly combines distinct conditional models together to provide enhanced control over samples.
- [ ] relevant | `2404.07724v2` | Applying Guidance in a Limited Interval Improves Sample and Distribution Quality in Diffusion Models | Guidance is a crucial technique for extracting the best performance out of image-generating diffusion models.
- [ ] relevant | `2408.09000v2` | Classifier-Free Guidance is a Predictor-Corrector | We investigate the theoretical foundations of classifier-free guidance (CFG).
- [ ] relevant | `2505.21101v1` | Conditional Diffusion Models with Classifier-Free Gibbs-like Guidance | Classifier-Free Guidance (CFG) is a widely used technique for improving conditional diffusion models by linearly combining the outputs of conditional and unconditional denoisers.
- [ ] relevant | `2507.05482v3` | Stein Diffusion Guidance: Training-Free Posterior Correction for Sampling Beyond High-Density Regions | Training-free diffusion guidance offers a flexible framework for leveraging off-the-shelf classifiers without additional training.
- [ ] relevant | `2507.08965v2` | Improving Classifier-Free Guidance in Masked Diffusion: Low-Dim Theoretical Insights with High-Dim Impact | Classifier-Free Guidance (CFG) is a widely used technique for conditional generation and improving sample quality in continuous diffusion models, and its extensions to discrete diffusion has recently started to be investigated.
- [x] relevant (gold) | `2509.22007v2` | Stage-wise Dynamics of Classifier-Free Guidance in Diffusion Models | Classifier-Free Guidance (CFG) is widely used to improve conditional fidelity in diffusion models, but its impact on sampling dynamics remains poorly understood.
- [ ] relevant | `2511.05844v3` | Enhancing Diffusion Model Guidance through Calibration and Regularization | Classifier-guided diffusion models have emerged as a powerful approach for conditional image generation, but they suffer from overconfident predictions during early denoising steps, causing the guidance gradient to vanish.
- [ ] relevant | `2605.28036v1` | Stay Fair! Ensuring Group Fairness in Diffusion Models Across Guidance Scales | Diffusion models steer conditional generation with a tunable guidance scale to trade off prompt alignment and diversity.

## Q04

**Question:** For generative models that work by progressively unmasking tokens, at what point in sampling does strong guidance hurt quality and at what point does it help?

**Gold:** `2507.08965v2` | Improving Classifier-Free Guidance in Masked Diffusion: Low-Dim Theoretical Insights with High-Dim Impact

> Classifier-Free Guidance (CFG) is a widely used technique for conditional generation and improving sample quality in continuous diffusion models, and its extensions to discrete diffusion has recently started to be investigated. In order to improve the algorithms in a principled way, this paper starts by analyzing the exact effect of CFG in the context of a low-dimensional masked diffusion model, with a special emphasis on the guidance schedule.

**Candidates:**

- [ ] relevant | `2207.12598v1` | Classifier-Free Diffusion Guidance | Classifier guidance is a recently introduced method to trade off mode coverage and sample fidelity in conditional diffusion models post training, in the same spirit as low temperature sampling or truncation in other types of generative models.
- [ ] relevant | `2311.00938v1` | Bridging the Gap: Addressing Discrepancies in Diffusion Model Training for Classifier-Free Guidance | Diffusion models have emerged as a pivotal advancement in generative models, setting new standards to the quality of the generated instances.
- [ ] relevant | `2404.01709v1` | Upsample Guidance: Scale Up Diffusion Models without Training | Diffusion models have demonstrated superior performance across various generative tasks including images, videos, and audio.
- [ ] relevant | `2404.07724v2` | Applying Guidance in a Limited Interval Improves Sample and Distribution Quality in Diffusion Models | Guidance is a crucial technique for extracting the best performance out of image-generating diffusion models.
- [ ] relevant | `2408.09000v2` | Classifier-Free Guidance is a Predictor-Corrector | We investigate the theoretical foundations of classifier-free guidance (CFG).
- [ ] relevant | `2412.09966v1` | EP-CFG: Energy-Preserving Classifier-Free Guidance | Classifier-free guidance (CFG) is widely used in diffusion models but often introduces over-contrast and over-saturation artifacts at higher guidance strengths.
- [ ] relevant | `2502.10574v1` | Classifier-free Guidance with Adaptive Scaling | Classifier-free guidance (CFG) is an essential mechanism in contemporary text-driven diffusion models.
- [ ] relevant | `2505.20199v1` | Adaptive Classifier-Free Guidance via Dynamic Low-Confidence Masking | Classifier-Free Guidance (CFG) significantly enhances controllability in generative models by interpolating conditional and unconditional predictions.
- [ ] relevant | `2506.10036v2` | Token Perturbation Guidance for Diffusion Models | Classifier-free guidance (CFG) has become an essential component of modern diffusion models to enhance both generation quality and alignment with input conditions.
- [x] relevant (gold) | `2507.08965v2` | Improving Classifier-Free Guidance in Masked Diffusion: Low-Dim Theoretical Insights with High-Dim Impact | Classifier-Free Guidance (CFG) is a widely used technique for conditional generation and improving sample quality in continuous diffusion models, and its extensions to discrete diffusion has recently started to be investigated.
- [ ] relevant | `2509.22007v2` | Stage-wise Dynamics of Classifier-Free Guidance in Diffusion Models | Classifier-Free Guidance (CFG) is widely used to improve conditional fidelity in diffusion models, but its impact on sampling dynamics remains poorly understood.
- [ ] relevant | `2510.11057v1` | Temporal Alignment Guidance: On-Manifold Sampling in Diffusion Models | Diffusion models have achieved remarkable success as generative models.
- [ ] relevant | `2512.17303v1` | EMAG: Self-Rectifying Diffusion Sampling with Exponential Moving Average Guidance | In diffusion and flow-matching generative models, guidance techniques are widely used to improve sample quality and consistency.

## Q05

**Question:** What has been proposed as the underlying cause of poor invertibility and mode collapse in guided text-to-image sampling, and what fix follows from treating text conditioning as an inverse problem?

**Gold:** `2406.08070v2` | CFG++: Manifold-constrained Classifier Free Guidance for Diffusion Models

> Classifier-free guidance (CFG) is a fundamental tool in modern diffusion models for text-guided generation. Although effective, CFG has notable drawbacks.

**Candidates:**

- [ ] relevant | `2301.11558v1` | Accelerating Guided Diffusion Sampling with Splitting Numerical Methods | Guided diffusion is a technique for conditioning the output of a diffusion model at sampling time without retraining the network for each specific task.
- [ ] relevant | `2303.04291v2` | Diffusion in the Dark: A Diffusion Model for Low-Light Text Recognition | Capturing images is a key part of automation for high-level tasks such as scene text recognition.
- [ ] relevant | `2303.07909v3` | Text-to-image Diffusion Models in Generative AI: A Survey | This survey reviews the progress of diffusion models in generating images from text, ~\textit{i.e.} text-to-image diffusion models.
- [ ] relevant | `2305.16223v2` | Prompt-Free Diffusion: Taking "Text" out of Text-to-Image Diffusion Models | Text-to-image (T2I) research has grown explosively in the past year, owing to the large-scale pre-trained diffusion models and many emerging personalization and editing approaches.
- [ ] relevant | `2306.05414v3` | Improving Tuning-Free Real Image Editing with Proximal Guidance | DDIM inversion has revealed the remarkable potential of real image editing within diffusion-based methods.
- [ ] relevant | `2401.03221v1` | MirrorDiffusion: Stabilizing Diffusion Process in Zero-shot Image Translation by Prompts Redescription and Beyond | Recently, text-to-image diffusion models become a new paradigm in image processing fields, including content generation, image restoration and image-to-image translation.
- [ ] relevant | `2403.04279v2` | Controllable Generation with Text-to-Image Diffusion Models: A Survey | In the rapidly advancing realm of visual generation, diffusion models have revolutionized the landscape, marking a significant shift in capabilities with their impressive text-guided generative functions.
- [x] relevant (gold) | `2406.08070v2` | CFG++: Manifold-constrained Classifier Free Guidance for Diffusion Models | Classifier-free guidance (CFG) is a fundamental tool in modern diffusion models for text-guided generation.
- [ ] relevant | `2408.09000v2` | Classifier-Free Guidance is a Predictor-Corrector | We investigate the theoretical foundations of classifier-free guidance (CFG).
- [ ] relevant | `2502.10574v1` | Classifier-free Guidance with Adaptive Scaling | Classifier-free guidance (CFG) is an essential mechanism in contemporary text-driven diffusion models.
- [ ] relevant | `2505.09571v1` | Don't Forget your Inverse DDIM for Image Editing | The field of text-to-image generation has undergone significant advancements with the introduction of diffusion models.
- [ ] relevant | `2506.08351v1` | How Much To Guide: Revisiting Adaptive Guidance in Classifier-Free Guidance Text-to-Vision Diffusion Models | With the rapid development of text-to-vision generation diffusion models, classifier-free guidance has emerged as the most prevalent method for conditioning.
- [ ] relevant | `2506.24108v3` | Navigating with Annealing Guidance Scale in Diffusion Space | Denoising diffusion models excel at generating high-quality images conditioned on text prompts, yet their effectiveness heavily relies on careful guidance during the sampling process.
- [ ] relevant | `2507.18654v2` | Diffusion Models for Solving Inverse Problems via Posterior Sampling with Piecewise Guidance | Diffusion models are powerful tools for sampling from high-dimensional distributions by progressively transforming pure noise into structured data through a denoising process.

## Q06

**Question:** Can noising and then denoising a maliciously perturbed histopathology image protect a classifier, and how much of the original accuracy is recovered?

**Gold:** `2301.06871v1` | Denoising Diffusion Probabilistic Models as a Defense against Adversarial Attacks

> Neural Networks are infamously sensitive to small perturbations in their inputs, making them vulnerable to adversarial attacks. This project evaluates the performance of Denoising Diffusion Probabilistic Models (DDPM) as a purification technique to defend against adversarial attacks.

**Candidates:**

- [ ] relevant | `2111.06399v1` | Selective Synthetic Augmentation with HistoGAN for Improved Histopathology Image Classification | Histopathological analysis is the present gold standard for precancerous lesion diagnosis.
- [ ] relevant | `2201.09865v4` | RePaint: Inpainting using Denoising Diffusion Probabilistic Models | Free-form inpainting is the task of adding new content to an image in the regions specified by an arbitrary binary mask.
- [ ] relevant | `2209.06167v2` | PET image denoising based on denoising diffusion probabilistic models | Due to various physical degradation factors and limited counts received, PET image quality needs further improvements.
- [x] relevant (gold) | `2301.06871v1` | Denoising Diffusion Probabilistic Models as a Defense against Adversarial Attacks | Neural Networks are infamously sensitive to small perturbations in their inputs, making them vulnerable to adversarial attacks.
- [ ] relevant | `2306.07440v1` | Deep Ultrasound Denoising Using Diffusion Probabilistic Models | Ultrasound images are widespread in medical diagnosis for musculoskeletal, cardiac, and obstetrical imaging due to the efficiency and non-invasiveness of the acquisition methodology.
- [ ] relevant | `2311.10868v1` | SDDPM: Speckle Denoising Diffusion Probabilistic Models | Coherent imaging systems, such as medical ultrasound and synthetic aperture radar (SAR), are subject to corruption from speckle due to sub-resolution scatterers.
- [ ] relevant | `2402.02316v4` | Your Diffusion Model is Secretly a Certifiably Robust Classifier | Generative learning, recognized for its effective modeling of data distributions, offers inherent advantages in handling out-of-distribution instances, especially for enhancing robustness to adversarial attacks.
- [ ] relevant | `2403.17377v2` | Self-Rectifying Diffusion Sampling with Perturbed-Attention Guidance | Recent studies have demonstrated that diffusion models are capable of generating high-quality samples, but their quality heavily depends on sampling guidance techniques, such as classifier guidance (CG) and classifier-free guidance (CFG).
- [ ] relevant | `2406.17399v1` | GradCheck: Analyzing classifier guidance gradients for conditional diffusion sampling | To sample from an unconditionally trained Denoising Diffusion Probabilistic Model (DDPM), classifier guidance adds conditional information during sampling, but the gradients from classifiers, especially those not trained on noisy images, are often unstable.
- [ ] relevant | `2411.16738v2` | Classifier-Free Guidance inside the Attraction Basin May Cause Memorization | Diffusion models are prone to exactly reproduce images from the training data.
- [ ] relevant | `2508.02903v1` | RDDPM: Robust Denoising Diffusion Probabilistic Model for Unsupervised Anomaly Segmentation | Recent advancements in diffusion models have demonstrated significant success in unsupervised anomaly segmentation.
- [ ] relevant | `2601.07253v1` | Universal Adversarial Purification with DDIM Metric Loss for Stable Diffusion | Stable Diffusion (SD) often produces degraded outputs when the training dataset contains adversarial noise.

## Q07

**Question:** How can images poisoned to disrupt a latent text-to-image model be cleaned when the attack targets its encoder, its denoiser, or both?

**Gold:** `2601.07253v1` | Universal Adversarial Purification with DDIM Metric Loss for Stable Diffusion

> Stable Diffusion (SD) often produces degraded outputs when the training dataset contains adversarial noise. Adversarial purification offers a promising solution by removing adversarial noise from contaminated data.

**Candidates:**

- [ ] relevant | `2107.07675v1` | Beyond In-Place Corruption: Insertion and Deletion In Denoising Probabilistic Models | Denoising diffusion probabilistic models (DDPMs) have shown impressive results on sequence generation by iteratively corrupting each example and then learning to map corrupted versions back to the original.
- [ ] relevant | `2201.09865v4` | RePaint: Inpainting using Denoising Diffusion Probabilistic Models | Free-form inpainting is the task of adding new content to an image in the regions specified by an arbitrary binary mask.
- [ ] relevant | `2206.02779v2` | Blended Latent Diffusion | The tremendous progress in neural image generation, coupled with the emergence of seemingly omnipotent vision-language models has finally enabled text-based interfaces for creating and editing images.
- [ ] relevant | `2210.12254v2` | Score-based Denoising Diffusion with Non-Isotropic Gaussian Noise Models | Generative models based on denoising diffusion techniques have led to an unprecedented increase in the quality and diversity of imagery that is now possible to create with neural generative models.
- [ ] relevant | `2301.06871v1` | Denoising Diffusion Probabilistic Models as a Defense against Adversarial Attacks | Neural Networks are infamously sensitive to small perturbations in their inputs, making them vulnerable to adversarial attacks.
- [ ] relevant | `2306.05720v2` | Beyond Surface Statistics: Scene Representations in a Latent Diffusion Model | Latent diffusion models (LDMs) exhibit an impressive ability to produce realistic images, yet the inner workings of these models remain mysterious.
- [ ] relevant | `2311.13619v1` | Steal My Artworks for Fine-tuning? A Watermarking Framework for Detecting Art Theft Mimicry in Text-to-Image Models | The advancement in text-to-image models has led to astonishing artistic performances.
- [ ] relevant | `2312.02156v2` | Latent Feature-Guided Diffusion Models for Shadow Removal | Recovering textures under shadows has remained a challenging problem due to the difficulty of inferring shadow-free scenes from shadow images.
- [ ] relevant | `2312.04410v1` | Smooth Diffusion: Crafting Smooth Latent Spaces in Diffusion Models | Recently, diffusion models have made remarkable progress in text-to-image (T2I) generation, synthesizing images with high fidelity and diverse contents.
- [ ] relevant | `2401.03221v1` | MirrorDiffusion: Stabilizing Diffusion Process in Zero-shot Image Translation by Prompts Redescription and Beyond | Recently, text-to-image diffusion models become a new paradigm in image processing fields, including content generation, image restoration and image-to-image translation.
- [ ] relevant | `2401.05779v4` | Erasing Undesirable Influence in Diffusion Models | Diffusion models are highly effective at generating high-quality images but pose risks, such as the unintentional generation of NSFW (not safe for work) content.
- [ ] relevant | `2403.04279v2` | Controllable Generation with Text-to-Image Diffusion Models: A Survey | In the rapidly advancing realm of visual generation, diffusion models have revolutionized the landscape, marking a significant shift in capabilities with their impressive text-guided generative functions.
- [ ] relevant | `2404.06666v3` | SafeGen: Mitigating Sexually Explicit Content Generation in Text-to-Image Models | Text-to-image (T2I) models, such as Stable Diffusion, have exhibited remarkable performance in generating high-quality images from text descriptions in recent years.
- [ ] relevant | `2407.21032v1` | Safeguard Text-to-Image Diffusion Models with Human Feedback Inversion | This paper addresses the societal concerns arising from large-scale text-to-image diffusion models for generating potentially harmful or copyrighted content.
- [ ] relevant | `2409.19365v3` | Conditional Image Synthesis with Diffusion Models: A Survey | Conditional image synthesis based on user-specified requirements is a key component in creating complex visual content.
- [ ] relevant | `2411.18956v1` | Random Sampling for Diffusion-based Adversarial Purification | Denoising Diffusion Probabilistic Models (DDPMs) have gained great attention in adversarial purification.
- [x] relevant (gold) | `2601.07253v1` | Universal Adversarial Purification with DDIM Metric Loss for Stable Diffusion | Stable Diffusion (SD) often produces degraded outputs when the training dataset contains adversarial noise.

## Q08

**Question:** Why might the usual stable reverse-sampling procedure be a poor fit when a diffusion model is used to cleanse attacked inputs, and what alternative sampling scheme adds more randomness?

**Gold:** `2411.18956v1` | Random Sampling for Diffusion-based Adversarial Purification

> Denoising Diffusion Probabilistic Models (DDPMs) have gained great attention in adversarial purification. Current diffusion-based works focus on designing effective condition-guided mechanisms while ignoring a fundamental problem, i.e., the original DDPM sampling is intended for stable generation, which may not be the optimal solution for adversarial purification.

**Candidates:**

- [ ] relevant | `2102.09672v1` | Improved Denoising Diffusion Probabilistic Models | Denoising diffusion probabilistic models (DDPM) are a class of generative models which have recently been shown to produce excellent samples.
- [ ] relevant | `2211.01364v3` | An optimal control perspective on diffusion-based generative modeling | We establish a connection between stochastic optimal control and generative models based on stochastic differential equations (SDEs), such as recently developed diffusion probabilistic models.
- [ ] relevant | `2301.06871v1` | Denoising Diffusion Probabilistic Models as a Defense against Adversarial Attacks | Neural Networks are infamously sensitive to small perturbations in their inputs, making them vulnerable to adversarial attacks.
- [ ] relevant | `2307.11118v1` | Diffusion Sampling with Momentum for Mitigating Divergence Artifacts | Despite the remarkable success of diffusion models in image generation, slow sampling remains a persistent issue.
- [ ] relevant | `2310.05264v5` | The Emergence of Reproducibility and Generalizability in Diffusion Models | In this work, we investigate an intriguing and prevalent phenomenon of diffusion models which we term as "consistent model reproducibility": given the same starting noise input and a deterministic sampler, different diffusion models often yield remarkably similar outputs.
- [ ] relevant | `2402.05098v4` | Improved off-policy training of diffusion samplers | We study the problem of training diffusion models to sample from a distribution with a given unnormalized density or energy function.
- [ ] relevant | `2402.07211v2` | Towards Fast Stochastic Sampling in Diffusion Generative Models | Diffusion models suffer from slow sample generation at inference time.
- [ ] relevant | `2404.07724v2` | Applying Guidance in a Limited Interval Improves Sample and Distribution Quality in Diffusion Models | Guidance is a crucial technique for extracting the best performance out of image-generating diffusion models.
- [x] relevant (gold) | `2411.18956v1` | Random Sampling for Diffusion-based Adversarial Purification | Denoising Diffusion Probabilistic Models (DDPMs) have gained great attention in adversarial purification.
- [ ] relevant | `2504.18130v3` | Score-based deterministic density sampling | We propose a deterministic sampling framework using Score-Based Transport Modeling for sampling an unnormalized target density $π$ given only its score $\nabla \log π$.
- [ ] relevant | `2506.06185v2` | Antithetic Noise in Diffusion Models | We systematically study antithetic initial noise in diffusion models, discovering that pairing each noise sample with its negation consistently produces strong negative correlation.
- [ ] relevant | `2510.11057v1` | Temporal Alignment Guidance: On-Manifold Sampling in Diffusion Models | Diffusion models have achieved remarkable success as generative models.
- [ ] relevant | `2601.21868v2` | On Forgetting and Stability of Score-based Generative models | Understanding the stability and long-time behavior of generative models is a fundamental problem in modern machine learning.
- [ ] relevant | `2605.06831v2` | Why DDIM Hallucinates More Than DDPM: A Theoretical Analysis of Reverse Dynamics | We theoretically study the hallucination phenomena in two canonical diffusion samplers: the stochastic Denoising Diffusion Probabilistic Model (DDPM) and the deterministic Denoising Diffusion Implicit Model (DDIM).
- [ ] relevant | `2605.22586v3` | A Tutorial on Diffusion Theory: From Differential Equations to Diffusion Models | Diffusion models have emerged as a dominant framework for generative modeling, but their mathematical foundations are often presented separately through diffusion probabilistic models, score-based modeling, stochastic differential equations, and numerical sampling methods.
- [ ] relevant | `2605.30330v1` | When, why, and how do diffusion posterior samplers fail? A finite-sample lens | Diffusion models have excellent capacity to model complex distributions of natural data, which has made them a popular and effective choice for posterior sampling in imaging inverse problems.

## Q09

**Question:** How can a generative model that learns gradients of log-densities be used to test whether two variables are independent given a third, while controlling the false-positive rate?

**Gold:** `2505.23309v1` | Score-based Generative Modeling for Conditional Independence Testing

> Determining conditional independence (CI) relationships between random variables is a fundamental yet challenging task in machine learning and statistics, especially in high-dimensional settings. Existing generative model-based CI testing methods, such as those utilizing generative adversarial networks (GANs), often struggle with undesirable modeling of conditional distributions and training instability, resulting in subpar performance.

**Candidates:**

- [ ] relevant | `2102.09672v1` | Improved Denoising Diffusion Probabilistic Models | Denoising diffusion probabilistic models (DDPM) are a class of generative models which have recently been shown to produce excellent samples.
- [ ] relevant | `2111.13606v1` | Conditional Image Generation with Score-Based Diffusion Models | Score-based diffusion models have emerged as one of the most promising frameworks for deep generative modelling.
- [ ] relevant | `2203.04698v1` | Score-Based Generative Models for Molecule Generation | Recent advances in generative models have made exploring design spaces easier for de novo molecule generation.
- [ ] relevant | `2207.12598v1` | Classifier-Free Diffusion Guidance | Classifier guidance is a recently introduced method to trade off mode coverage and sample fidelity in conditional diffusion models post training, in the same spirit as low temperature sampling or truncation in other types of generative models.
- [ ] relevant | `2211.01364v3` | An optimal control perspective on diffusion-based generative modeling | We establish a connection between stochastic optimal control and generative models based on stochastic differential equations (SDEs), such as recently developed diffusion probabilistic models.
- [ ] relevant | `2302.04411v1` | Geometry of Score Based Generative Models | In this work, we look at Score-based generative models (also called diffusion generative models) from a geometric perspective.
- [ ] relevant | `2305.16150v3` | Unifying GANs and Score-Based Diffusion as Generative Particle Models | Particle-based deep generative models, such as gradient flows and score-based diffusion models, have recently gained traction thanks to their striking performance.
- [ ] relevant | `2311.09952v1` | Score-based generative models learn manifold-like structures with constrained mixing | How do score-based generative models (SBMs) learn the data distribution supported on a low-dimensional manifold?
- [ ] relevant | `2407.00626v2` | Maximum Entropy Inverse Reinforcement Learning of Diffusion Models with Energy-Based Models | We present a maximum entropy inverse reinforcement learning (IRL) approach for improving the sample quality of diffusion generative models, especially when the number of generation time steps is small.
- [ ] relevant | `2502.17100v4` | Generative Models in Decision Making: A Survey | Generative models have fundamentally reshaped the landscape of decision-making, reframing the problem from pure scalar reward maximization to high-fidelity trajectory generation and distribution matching.
- [ ] relevant | `2504.18130v3` | Score-based deterministic density sampling | We propose a deterministic sampling framework using Score-Based Transport Modeling for sampling an unnormalized target density $π$ given only its score $\nabla \log π$.
- [ ] relevant | `2505.21101v1` | Conditional Diffusion Models with Classifier-Free Gibbs-like Guidance | Classifier-Free Guidance (CFG) is a widely used technique for improving conditional diffusion models by linearly combining the outputs of conditional and unconditional denoisers.
- [x] relevant (gold) | `2505.23309v1` | Score-based Generative Modeling for Conditional Independence Testing | Determining conditional independence (CI) relationships between random variables is a fundamental yet challenging task in machine learning and statistics, especially in high-dimensional settings.
- [ ] relevant | `2507.04794v1` | Generalization bounds for score-based generative models: a synthetic proof | We establish minimax convergence rates for score-based generative models (SGMs) under the $1$-Wasserstein distance.
- [ ] relevant | `2601.19368v1` | Divergence-Free Diffusion Models for Incompressible Fluid Flows | Generative diffusion models are extensively used in unsupervised and self-supervised machine learning with the aim to generate new samples from a probability distribution estimated with a set of known samples.

## Q10

**Question:** How can the output of a GAN serve as a starting point for a diffusion model that converts between medical imaging modalities and also reports uncertainty?

**Gold:** `2405.12223v3` | Cascaded Multi-path Shortcut Diffusion Model for Medical Image Translation

> Image-to-image translation is a vital component in medical imaging processing, with many uses in a wide range of imaging modalities and clinical scenarios. Previous methods include Generative Adversarial Networks (GANs) and Diffusion Models (DMs), which offer realism but suffer from instability and lack uncertainty estimation.

**Candidates:**

- [ ] relevant | `2006.11239v2` | Denoising Diffusion Probabilistic Models | We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.
- [ ] relevant | `2102.09672v1` | Improved Denoising Diffusion Probabilistic Models | Denoising diffusion probabilistic models (DDPM) are a class of generative models which have recently been shown to produce excellent samples.
- [ ] relevant | `2110.05243v3` | Score-based diffusion models for accelerated MRI | Score-based diffusion models provide a powerful way to model images using the gradient of the data distribution.
- [ ] relevant | `2111.02316v1` | Improving Model Compatibility of Generative Adversarial Networks by Boundary Calibration | Generative Adversarial Networks (GANs) is a powerful family of models that learn an underlying distribution to generate synthetic data.
- [ ] relevant | `2206.02262v4` | Diffusion-GAN: Training GANs with Diffusion | Generative adversarial networks (GANs) are challenging to train stably, and a promising remedy of injecting instance noise into the discriminator input has not been very effective in practice.
- [ ] relevant | `2210.12254v2` | Score-based Denoising Diffusion with Non-Isotropic Gaussian Noise Models | Generative models based on denoising diffusion techniques have led to an unprecedented increase in the quality and diversity of imagery that is now possible to create with neural generative models.
- [ ] relevant | `2305.16150v3` | Unifying GANs and Score-Based Diffusion as Generative Particle Models | Particle-based deep generative models, such as gradient flows and score-based diffusion models, have recently gained traction thanks to their striking performance.
- [ ] relevant | `2310.10414v3` | Style transfer between Microscopy and Magnetic Resonance Imaging via Generative Adversarial Network in small sample size settings | Cross-modal augmentation of Magnetic Resonance Imaging (MRI) and microscopic imaging based on the same tissue samples is promising because it can allow histopathological analysis in the absence of an underlying invasive biopsy procedure.
- [ ] relevant | `2311.04552v1` | A 3D generative model of pathological multi-modal MR images and segmentations | Generative modelling and synthetic data can be a surrogate for real medical imaging datasets, whose scarcity and difficulty to share can be a nuisance when delivering accurate deep learning models for healthcare applications.
- [x] relevant (gold) | `2405.12223v3` | Cascaded Multi-path Shortcut Diffusion Model for Medical Image Translation | Image-to-image translation is a vital component in medical imaging processing, with many uses in a wide range of imaging modalities and clinical scenarios.
- [ ] relevant | `2410.19288v1` | A Flow-based Truncated Denoising Diffusion Model for Super-resolution Magnetic Resonance Spectroscopic Imaging | Magnetic Resonance Spectroscopic Imaging (MRSI) is a non-invasive imaging technique for studying metabolism and has become a crucial tool for understanding neurological diseases, cancers and diabetes.
- [ ] relevant | `2509.17790v1` | Conditional Diffusion Models for CT Image Synthesis from CBCT: A Systematic Review | Objective: Cone-beam computed tomography (CBCT) provides a low-dose imaging alternative to conventional CT, but suffers from noise, scatter, and artifacts that degrade image quality.

## Q11

**Question:** Can a natural-language description of a task be used to generate the parameters of a neural network for an unseen task without any fine-tuning?

**Gold:** `2210.08942v2` | Meta-Learning via Classifier(-free) Diffusion Guidance

> We introduce meta-learning algorithms that perform zero-shot weight-space adaptation of neural network models to unseen tasks. Our methods repurpose the popular generative image synthesis techniques of natural language guidance and diffusion models to generate neural network weights adapted for tasks.

**Candidates:**

- [ ] relevant | `2206.01714v6` | Compositional Visual Generation with Composable Diffusion Models | Large text-guided diffusion models, such as DALLE-2, are able to generate stunning photorealistic images given natural language descriptions.
- [x] relevant (gold) | `2210.08942v2` | Meta-Learning via Classifier(-free) Diffusion Guidance | We introduce meta-learning algorithms that perform zero-shot weight-space adaptation of neural network models to unseen tasks.
- [ ] relevant | `2212.00006v1` | Operationalizing Specifications, In Addition to Test Sets for Evaluating Constrained Generative Models | In this work, we present some recommendations on the evaluation of state-of-the-art generative models for constrained generation tasks.
- [ ] relevant | `2212.04488v2` | Multi-Concept Customization of Text-to-Image Diffusion | While generative models produce high-quality images of concepts learned from a large-scale database, a user often wishes to synthesize instantiations of their own concepts (for example, their family, pets, or items).
- [ ] relevant | `2304.04746v1` | A Cheaper and Better Diffusion Language Model with Soft-Masked Noise | Diffusion models that are based on iterative denoising have been recently proposed and leveraged in various generation tasks like image generation.
- [ ] relevant | `2304.09116v3` | NaturalSpeech 2: Latent Diffusion Models are Natural and Zero-Shot Speech and Singing Synthesizers | Scaling text-to-speech (TTS) to large-scale, multi-speaker, and in-the-wild datasets is important to capture the diversity in human speech such as speaker identities, prosodies, and styles (e.g., singing).
- [ ] relevant | `2312.08195v2` | Image is All You Need to Empower Large-scale Diffusion Models for In-Domain Generation | In-domain generation aims to perform a variety of tasks within a specific domain, such as unconditional generation, text-to-image, image editing, 3D generation, and more.
- [ ] relevant | `2402.13144v3` | Neural Network Diffusion | Diffusion models have achieved remarkable success in image and video generation.
- [ ] relevant | `2411.05706v1` | Image2Text2Image: A Novel Framework for Label-Free Evaluation of Image-to-Text Generation with Text-to-Image Diffusion Models | Evaluating the quality of automatically generated image descriptions is a complex task that requires metrics capturing various dimensions, such as grammaticality, coverage, accuracy, and truthfulness.
- [ ] relevant | `2501.13926v2` | Can We Generate Images with CoT? Let's Verify and Reinforce Image Generation Step by Step | Chain-of-Thought (CoT) reasoning has been extensively explored in large models to tackle complex understanding tasks.
- [ ] relevant | `2505.20199v1` | Adaptive Classifier-Free Guidance via Dynamic Low-Confidence Masking | Classifier-Free Guidance (CFG) significantly enhances controllability in generative models by interpolating conditional and unconditional predictions.
- [ ] relevant | `2506.10395v2` | Pisces: An Auto-regressive Foundation Model for Image Understanding and Generation | Recent advances in large language models (LLMs) have enabled multimodal foundation models to tackle both image understanding and generation within a unified framework.
- [ ] relevant | `2509.16131v2` | Dynamic Classifier-Free Diffusion Guidance via Online Feedback | Classifier-free guidance (CFG) is a cornerstone of text-to-image diffusion models, yet its effectiveness is limited by the use of static guidance scales.
- [ ] relevant | `2601.22468v1` | Training-Free Representation Guidance for Diffusion Models with a Representation Alignment Projector | Recent progress in generative modeling has enabled high-quality visual synthesis with diffusion-based frameworks, supporting controllable sampling and large-scale training.

## Q12

**Question:** How can keyframes, sketches or depth maps be used to steer a video generator without fine-tuning the model?

**Gold:** `2506.07177v2` | Frame Guidance: Training-Free Guidance for Frame-Level Control in Video Diffusion Models

> Advancements in diffusion models have significantly improved video quality, directing attention to fine-grained controllability. However, many existing methods depend on fine-tuning large-scale video models for specific tasks, which becomes increasingly impractical as model sizes continue to grow.

**Candidates:**

- [ ] relevant | `2301.03949v2` | Modiff: Action-Conditioned 3D Motion Generation with Denoising Diffusion Probabilistic Models | Diffusion-based generative models have recently emerged as powerful solutions for high-quality synthesis in multiple domains.
- [ ] relevant | `2304.03373v2` | Training-Free Layout Control with Cross-Attention Guidance | Recent diffusion-based generators can produce high-quality images from textual prompts.
- [ ] relevant | `2304.08477v2` | Latent-Shift: Latent Diffusion with Temporal Shift for Efficient Text-to-Video Generation | We propose Latent-Shift -- an efficient text-to-video generation method based on a pretrained text-to-image generation model that consists of an autoencoder and a U-Net diffusion model.
- [ ] relevant | `2306.09274v1` | Conditional Human Sketch Synthesis with Explicit Abstraction Control | This paper presents a novel free-hand sketch synthesis approach addressing explicit abstraction control in class-conditional and photo-to-sketch synthesis.
- [ ] relevant | `2311.03226v1` | LDM3D-VR: Latent Diffusion Model for 3D VR | Latent diffusion models have proven to be state-of-the-art in the creation and manipulation of visual outputs.
- [ ] relevant | `2312.08195v2` | Image is All You Need to Empower Large-scale Diffusion Models for In-Domain Generation | In-domain generation aims to perform a variety of tasks within a specific domain, such as unconditional generation, text-to-image, image editing, 3D generation, and more.
- [ ] relevant | `2404.01709v1` | Upsample Guidance: Scale Up Diffusion Models without Training | Diffusion models have demonstrated superior performance across various generative tasks including images, videos, and audio.
- [ ] relevant | `2405.03150v2` | Video Diffusion Models: A Survey | Diffusion generative models have recently become a powerful technique for creating and modifying high-quality, coherent video content.
- [ ] relevant | `2411.18664v1` | Spatiotemporal Skip Guidance for Enhanced Video Diffusion Sampling | Diffusion models have emerged as a powerful tool for generating high-quality images, videos, and 3D content.
- [ ] relevant | `2412.06029v1` | Latent-Reframe: Enabling Camera Control for Video Diffusion Model without Training | Precise camera pose control is crucial for video generation with diffusion models.
- [x] relevant (gold) | `2506.07177v2` | Frame Guidance: Training-Free Guidance for Frame-Level Control in Video Diffusion Models | Advancements in diffusion models have significantly improved video quality, directing attention to fine-grained controllability.
- [ ] relevant | `2506.10005v1` | Multimodal Cinematic Video Synthesis Using Text-to-Image and Audio Generation Models | Advances in generative artificial intelligence have altered multimedia creation, allowing for automatic cinematic video synthesis from text inputs.
- [ ] relevant | `2606.09828v1` | Latent Spatial Memory for Video World Models | Video world models that maintain 3D spatial consistency across generated frames typically rely on explicit point cloud memory constructed in RGB space.

## Q13

**Question:** How can a model that generates sung vocals be trained when most of the available audio has no aligned lyrics or pitch annotations?

**Gold:** `2406.05965v1` | MakeSinger: A Semi-Supervised Training Method for Data-Efficient Singing Voice Synthesis via Classifier-free Diffusion Guidance

> In this paper, we propose MakeSinger, a semi-supervised training method for singing voice synthesis (SVS) via classifier-free diffusion guidance. The challenge in SVS lies in the costly process of gathering aligned sets of text, pitch, and audio data.

**Candidates:**

- [ ] relevant | `2106.05931v3` | Score-based Generative Modeling in Latent Space | Score-based generative models (SGMs) have recently demonstrated impressive results in terms of both sample quality and distribution coverage.
- [ ] relevant | `2212.06359v1` | Score-based Generative Modeling Secretly Minimizes the Wasserstein Distance | Score-based generative models are shown to achieve remarkable empirical performances in various applications such as image generation and audio synthesis.
- [ ] relevant | `2304.09116v3` | NaturalSpeech 2: Latent Diffusion Models are Natural and Zero-Shot Speech and Singing Synthesizers | Scaling text-to-speech (TTS) to large-scale, multi-speaker, and in-the-wild datasets is important to capture the diversity in human speech such as speaker identities, prosodies, and styles (e.g., singing).
- [ ] relevant | `2308.14319v1` | Voice Conversion with Denoising Diffusion Probabilistic GAN Models | Voice conversion is a method that allows for the transformation of speaking style while maintaining the integrity of linguistic information.
- [ ] relevant | `2311.09952v1` | Score-based generative models learn manifold-like structures with constrained mixing | How do score-based generative models (SBMs) learn the data distribution supported on a low-dimensional manifold?
- [ ] relevant | `2402.13144v3` | Neural Network Diffusion | Diffusion models have achieved remarkable success in image and video generation.
- [ ] relevant | `2404.01709v1` | Upsample Guidance: Scale Up Diffusion Models without Training | Diffusion models have demonstrated superior performance across various generative tasks including images, videos, and audio.
- [x] relevant (gold) | `2406.05965v1` | MakeSinger: A Semi-Supervised Training Method for Data-Efficient Singing Voice Synthesis via Classifier-free Diffusion Guidance | In this paper, we propose MakeSinger, a semi-supervised training method for singing voice synthesis (SVS) via classifier-free diffusion guidance.
- [ ] relevant | `2409.09401v2` | Towards Diverse and Efficient Audio Captioning via Diffusion Models | We introduce Diffusion-based Audio Captioning (DAC), a non-autoregressive diffusion model tailored for diverse and efficient audio captioning.
- [ ] relevant | `2509.22728v2` | Prompt-aware classifier free guidance for diffusion models | Diffusion models have achieved remarkable progress in image and audio generation, largely due to Classifier-Free Guidance.
- [ ] relevant | `2510.11057v1` | Temporal Alignment Guidance: On-Manifold Sampling in Diffusion Models | Diffusion models have achieved remarkable success as generative models.
- [ ] relevant | `2601.22468v1` | Training-Free Representation Guidance for Diffusion Models with a Representation Alignment Projector | Recent progress in generative modeling has enabled high-quality visual synthesis with diffusion-based frameworks, supporting controllable sampling and large-scale training.

## Q14

**Question:** According to an overview of diffusion-based video generation, what are the main open challenges for the field?

**Gold:** `2405.03150v2` | Video Diffusion Models: A Survey

> Diffusion generative models have recently become a powerful technique for creating and modifying high-quality, coherent video content. This survey provides a comprehensive overview of the critical components of diffusion models for video generation, including their applications, architectural design, and temporal dynamics modeling.

**Candidates:**

- [ ] relevant | `2111.13606v1` | Conditional Image Generation with Score-Based Diffusion Models | Score-based diffusion models have emerged as one of the most promising frameworks for deep generative modelling.
- [ ] relevant | `2303.02490v2` | Diffusion Models Generate Images Like Painters: an Analytical Theory of Outline First, Details Later | How do diffusion generative models convert pure noise into meaningful images?
- [ ] relevant | `2402.13144v3` | Neural Network Diffusion | Diffusion models have achieved remarkable success in image and video generation.
- [ ] relevant | `2403.04279v2` | Controllable Generation with Text-to-Image Diffusion Models: A Survey | In the rapidly advancing realm of visual generation, diffusion models have revolutionized the landscape, marking a significant shift in capabilities with their impressive text-guided generative functions.
- [ ] relevant | `2404.01709v1` | Upsample Guidance: Scale Up Diffusion Models without Training | Diffusion models have demonstrated superior performance across various generative tasks including images, videos, and audio.
- [x] relevant (gold) | `2405.03150v2` | Video Diffusion Models: A Survey | Diffusion generative models have recently become a powerful technique for creating and modifying high-quality, coherent video content.
- [ ] relevant | `2405.11473v4` | FIFO-Diffusion: Generating Infinite Videos from Text without Training | We propose a novel inference technique based on a pretrained diffusion model for text-conditional video generation.
- [ ] relevant | `2409.09401v2` | Towards Diverse and Efficient Audio Captioning via Diffusion Models | We introduce Diffusion-based Audio Captioning (DAC), a non-autoregressive diffusion model tailored for diverse and efficient audio captioning.
- [ ] relevant | `2411.18664v1` | Spatiotemporal Skip Guidance for Enhanced Video Diffusion Sampling | Diffusion models have emerged as a powerful tool for generating high-quality images, videos, and 3D content.
- [ ] relevant | `2412.06029v1` | Latent-Reframe: Enabling Camera Control for Video Diffusion Model without Training | Precise camera pose control is crucial for video generation with diffusion models.
- [ ] relevant | `2506.07177v2` | Frame Guidance: Training-Free Guidance for Frame-Level Control in Video Diffusion Models | Advancements in diffusion models have significantly improved video quality, directing attention to fine-grained controllability.
- [ ] relevant | `2506.10005v1` | Multimodal Cinematic Video Synthesis Using Text-to-Image and Audio Generation Models | Advances in generative artificial intelligence have altered multimedia creation, allowing for automatic cinematic video synthesis from text inputs.

## Q15

**Question:** How can a real photograph be told apart from a diffusion-generated one by looking at how well a pretrained model can reproduce the image?

**Gold:** `2303.09295v1` | DIRE for Diffusion-Generated Image Detection

> Diffusion models have shown remarkable success in visual synthesis, but have also raised concerns about potential abuse for malicious purposes. In this paper, we seek to build a detector for telling apart real images from diffusion-generated images.

**Candidates:**

- [ ] relevant | `2006.11239v2` | Denoising Diffusion Probabilistic Models | We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.
- [ ] relevant | `2206.01714v6` | Compositional Visual Generation with Composable Diffusion Models | Large text-guided diffusion models, such as DALLE-2, are able to generate stunning photorealistic images given natural language descriptions.
- [ ] relevant | `2207.12598v1` | Classifier-Free Diffusion Guidance | Classifier guidance is a recently introduced method to trade off mode coverage and sample fidelity in conditional diffusion models post training, in the same spirit as low temperature sampling or truncation in other types of generative models.
- [ ] relevant | `2303.02490v2` | Diffusion Models Generate Images Like Painters: an Analytical Theory of Outline First, Details Later | How do diffusion generative models convert pure noise into meaningful images?
- [x] relevant (gold) | `2303.09295v1` | DIRE for Diffusion-Generated Image Detection | Diffusion models have shown remarkable success in visual synthesis, but have also raised concerns about potential abuse for malicious purposes.
- [ ] relevant | `2306.05720v2` | Beyond Surface Statistics: Scene Representations in a Latent Diffusion Model | Latent diffusion models (LDMs) exhibit an impressive ability to produce realistic images, yet the inner workings of these models remain mysterious.
- [ ] relevant | `2311.10892v1` | The Hidden Linear Structure in Score-Based Models and its Application | Score-based models have achieved remarkable results in the generative modeling of many domains.
- [ ] relevant | `2312.02246v4` | Conditional Variational Diffusion Models | Inverse problems aim to determine parameters from observations, a crucial task in engineering and science.
- [ ] relevant | `2312.07586v5` | Characteristic Guidance: Non-linear Correction for Diffusion Model at Large Guidance Scale | Popular guidance for denoising diffusion probabilistic model (DDPM) linearly combines distinct conditional models together to provide enhanced control over samples.
- [ ] relevant | `2402.16506v3` | Stochastic Conditional Diffusion Models for Robust Semantic Image Synthesis | Semantic image synthesis (SIS) is a task to generate realistic images corresponding to semantic maps (labels).
- [ ] relevant | `2403.04279v2` | Controllable Generation with Text-to-Image Diffusion Models: A Survey | In the rapidly advancing realm of visual generation, diffusion models have revolutionized the landscape, marking a significant shift in capabilities with their impressive text-guided generative functions.
- [ ] relevant | `2404.01709v1` | Upsample Guidance: Scale Up Diffusion Models without Training | Diffusion models have demonstrated superior performance across various generative tasks including images, videos, and audio.
- [ ] relevant | `2404.07724v2` | Applying Guidance in a Limited Interval Improves Sample and Distribution Quality in Diffusion Models | Guidance is a crucial technique for extracting the best performance out of image-generating diffusion models.
- [ ] relevant | `2405.15891v3` | Score Distillation via Reparametrized DDIM | While 2D diffusion models generate realistic, high-detail images, 3D shape generation methods like Score Distillation Sampling (SDS) built on these 2D diffusion models produce cartoon-like, over-smoothed shapes.
- [ ] relevant | `2409.19365v3` | Conditional Image Synthesis with Diffusion Models: A Survey | Conditional image synthesis based on user-specified requirements is a key component in creating complex visual content.
- [ ] relevant | `2604.24877v1` | Learning Illumination Control in Diffusion Models | Controlling illumination in images is essential for photography and visual content creation.

## Q16

**Question:** How can the discrete-step probabilistic formulation, score-based SDEs, deterministic implicit samplers and flow matching all be explained within one differential-equation picture?

**Gold:** `2605.22586v3` | A Tutorial on Diffusion Theory: From Differential Equations to Diffusion Models

> Diffusion models have emerged as a dominant framework for generative modeling, but their mathematical foundations are often presented separately through diffusion probabilistic models, score-based modeling, stochastic differential equations, and numerical sampling methods. We write this tutorial to provide a unified and self-contained account of these viewpoints from the perspective of differential equations.

**Candidates:**

- [ ] relevant | `2006.11239v2` | Denoising Diffusion Probabilistic Models | We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.
- [ ] relevant | `2011.13456v2` | Score-Based Generative Modeling through Stochastic Differential Equations | Creating noise from data is easy; creating data from noise is generative modeling.
- [ ] relevant | `2110.05243v3` | Score-based diffusion models for accelerated MRI | Score-based diffusion models provide a powerful way to model images using the gradient of the data distribution.
- [ ] relevant | `2112.07068v4` | Score-Based Generative Modeling with Critically-Damped Langevin Diffusion | Score-based generative models (SGMs) have demonstrated remarkable synthesis quality.
- [ ] relevant | `2208.05003v1` | Wavelet Score-Based Generative Modeling | Score-based generative models (SGMs) synthesize new data samples from Gaussian white noise by running a time-reversed Stochastic Differential Equation (SDE) whose drift coefficient depends on some probabilistic score.
- [ ] relevant | `2211.01364v3` | An optimal control perspective on diffusion-based generative modeling | We establish a connection between stochastic optimal control and generative models based on stochastic differential equations (SDEs), such as recently developed diffusion probabilistic models.
- [ ] relevant | `2212.03325v1` | Proposal of a Score Based Approach to Sampling Using Monte Carlo Estimation of Score and Oracle Access to Target Density | Score based approaches to sampling have shown much success as a generative algorithm to produce new samples from a target density given a pool of initial samples.
- [ ] relevant | `2302.04411v1` | Geometry of Score Based Generative Models | In this work, we look at Score-based generative models (also called diffusion generative models) from a geometric perspective.
- [ ] relevant | `2312.10527v2` | CoCoGen: Physically-Consistent and Conditioned Score-based Generative Models for Forward and Inverse Problems | Recent advances in generative artificial intelligence have had a significant impact on diverse domains spanning computer vision, natural language processing, and drug discovery.
- [ ] relevant | `2405.15891v3` | Score Distillation via Reparametrized DDIM | While 2D diffusion models generate realistic, high-detail images, 3D shape generation methods like Score Distillation Sampling (SDS) built on these 2D diffusion models produce cartoon-like, over-smoothed shapes.
- [ ] relevant | `2408.07285v1` | DDIM Redux: Mathematical Foundation and Some Extension | This note provides a critical review of the mathematical concepts underlying the generalized diffusion denoising implicit model (gDDIM) and the exponential integrator (EI) scheme.
- [ ] relevant | `2412.20899v1` | DDIM sampling for Generative AIBIM, a faster intelligent structural design framework | Generative AIBIM, a successful structural design pipeline, has proven its ability to intelligently generate high-quality, diverse, and creative shear wall designs that are tailored to specific physical conditions.
- [ ] relevant | `2504.18130v3` | Score-based deterministic density sampling | We propose a deterministic sampling framework using Score-Based Transport Modeling for sampling an unnormalized target density $π$ given only its score $\nabla \log π$.
- [ ] relevant | `2603.28572v1` | Unrestrained Simplex Denoising for Discrete Data. A Non-Markovian Approach Applied to Graph Generation | Denoising models such as Diffusion or Flow Matching have recently advanced generative modeling for discrete structures, yet most approaches either operate directly in the discrete state space, causing abrupt state changes.
- [ ] relevant | `2605.06831v2` | Why DDIM Hallucinates More Than DDPM: A Theoretical Analysis of Reverse Dynamics | We theoretically study the hallucination phenomena in two canonical diffusion samplers: the stochastic Denoising Diffusion Probabilistic Model (DDPM) and the deterministic Denoising Diffusion Implicit Model (DDIM).
- [x] relevant (gold) | `2605.22586v3` | A Tutorial on Diffusion Theory: From Differential Equations to Diffusion Models | Diffusion models have emerged as a dominant framework for generative modeling, but their mathematical foundations are often presented separately through diffusion probabilistic models, score-based modeling, stochastic differential equations, and numerical sampling methods.

## Q17

**Question:** What is gained by learning the variances of the reverse process instead of fixing them, in terms of the number of network evaluations needed for sampling?

**Gold:** `2102.09672v1` | Improved Denoising Diffusion Probabilistic Models

> Denoising diffusion probabilistic models (DDPM) are a class of generative models which have recently been shown to produce excellent samples. We show that with a few simple modifications, DDPMs can also achieve competitive log-likelihoods while maintaining high sample quality.

**Candidates:**

- [ ] relevant | `2003.00638v1` | Permutation Invariant Graph Generation via Score-Based Generative Modeling | Learning generative models for graph-structured data is challenging because graphs are discrete, combinatorial, and the underlying data distribution is invariant to the ordering of nodes.
- [x] relevant (gold) | `2102.09672v1` | Improved Denoising Diffusion Probabilistic Models | Denoising diffusion probabilistic models (DDPM) are a class of generative models which have recently been shown to produce excellent samples.
- [ ] relevant | `2105.13695v1` | AutoSampling: Search for Effective Data Sampling Schedules | Data sampling acts as a pivotal role in training deep learning models.
- [ ] relevant | `2108.06084v4` | The Stability-Efficiency Dilemma: Investigating Sequence Length Warmup for Training GPT Models | Recent works have demonstrated great success in pre-training large-scale autoregressive language models on massive GPUs.
- [ ] relevant | `2310.05264v5` | The Emergence of Reproducibility and Generalizability in Diffusion Models | In this work, we investigate an intriguing and prevalent phenomenon of diffusion models which we term as "consistent model reproducibility": given the same starting noise input and a deterministic sampler, different diffusion models often yield remarkably similar outputs.
- [ ] relevant | `2312.02246v4` | Conditional Variational Diffusion Models | Inverse problems aim to determine parameters from observations, a crucial task in engineering and science.
- [ ] relevant | `2402.05098v4` | Improved off-policy training of diffusion samplers | We study the problem of training diffusion models to sample from a distribution with a given unnormalized density or energy function.
- [ ] relevant | `2404.07724v2` | Applying Guidance in a Limited Interval Improves Sample and Distribution Quality in Diffusion Models | Guidance is a crucial technique for extracting the best performance out of image-generating diffusion models.
- [ ] relevant | `2506.06185v2` | Antithetic Noise in Diffusion Models | We systematically study antithetic initial noise in diffusion models, discovering that pairing each noise sample with its negation consistently produces strong negative correlation.
- [ ] relevant | `2512.17303v1` | EMAG: Self-Rectifying Diffusion Sampling with Exponential Moving Average Guidance | In diffusion and flow-matching generative models, guidance techniques are widely used to improve sample quality and consistency.
- [ ] relevant | `2601.21868v2` | On Forgetting and Stability of Score-based Generative models | Understanding the stability and long-time behavior of generative models is a fundamental problem in modern machine learning.
- [ ] relevant | `2605.22586v3` | A Tutorial on Diffusion Theory: From Differential Equations to Diffusion Models | Diffusion models have emerged as a dominant framework for generative modeling, but their mathematical foundations are often presented separately through diffusion probabilistic models, score-based modeling, stochastic differential equations, and numerical sampling methods.
- [ ] relevant | `2605.30330v1` | When, why, and how do diffusion posterior samplers fail? A finite-sample lens | Diffusion models have excellent capacity to model complex distributions of natural data, which has made them a popular and effective choice for posterior sampling in imaging inverse problems.

## Q18

**Question:** Which exact mathematical results have been derived for the generalized deterministic implicit sampler and for exponential-integrator solvers?

**Gold:** `2408.07285v1` | DDIM Redux: Mathematical Foundation and Some Extension

> This note provides a critical review of the mathematical concepts underlying the generalized diffusion denoising implicit model (gDDIM) and the exponential integrator (EI) scheme. We present enhanced mathematical results, including an exact expression for the reverse trajectory in the probability flow ODE and an exact expression for the covariance matrix in the gDDIM scheme.

**Candidates:**

- [ ] relevant | `1706.09163v1` | Probabilistic and Piecewise Deterministic models in Biology | We present recent results on Piecewise Deterministic Markov Processes (PDMPs), involved in biological modeling.
- [ ] relevant | `2101.04525v2` | A comparison of optimisation algorithms for high-dimensional particle and astrophysics applications | Optimisation problems are ubiquitous in particle and astrophysics, and involve locating the optimum of a complicated function of many parameters that may be computationally expensive to evaluate.
- [ ] relevant | `2211.01364v3` | An optimal control perspective on diffusion-based generative modeling | We establish a connection between stochastic optimal control and generative models based on stochastic differential equations (SDEs), such as recently developed diffusion probabilistic models.
- [ ] relevant | `2307.11118v1` | Diffusion Sampling with Momentum for Mitigating Divergence Artifacts | Despite the remarkable success of diffusion models in image generation, slow sampling remains a persistent issue.
- [ ] relevant | `2402.05098v4` | Improved off-policy training of diffusion samplers | We study the problem of training diffusion models to sample from a distribution with a given unnormalized density or energy function.
- [ ] relevant | `2402.07211v2` | Towards Fast Stochastic Sampling in Diffusion Generative Models | Diffusion models suffer from slow sample generation at inference time.
- [x] relevant (gold) | `2408.07285v1` | DDIM Redux: Mathematical Foundation and Some Extension | This note provides a critical review of the mathematical concepts underlying the generalized diffusion denoising implicit model (gDDIM) and the exponential integrator (EI) scheme.
- [ ] relevant | `2410.09945v2` | Variational Diffusion Posterior Sampling with Midpoint Guidance | Diffusion models have recently shown considerable potential in solving Bayesian inverse problems when used as priors.
- [ ] relevant | `2504.18130v3` | Score-based deterministic density sampling | We propose a deterministic sampling framework using Score-Based Transport Modeling for sampling an unnormalized target density $π$ given only its score $\nabla \log π$.
- [ ] relevant | `2507.04794v1` | Generalization bounds for score-based generative models: a synthetic proof | We establish minimax convergence rates for score-based generative models (SGMs) under the $1$-Wasserstein distance.
- [ ] relevant | `2511.09180v1` | FSampler: Training Free Acceleration of Diffusion Sampling via Epsilon Extrapolation | FSampler is a training free, sampler agnostic execution layer that accelerates diffusion sampling by reducing the number of function evaluations (NFE).
- [ ] relevant | `2605.06831v2` | Why DDIM Hallucinates More Than DDPM: A Theoretical Analysis of Reverse Dynamics | We theoretically study the hallucination phenomena in two canonical diffusion samplers: the stochastic Denoising Diffusion Probabilistic Model (DDPM) and the deterministic Denoising Diffusion Implicit Model (DDIM).
- [ ] relevant | `2605.22586v3` | A Tutorial on Diffusion Theory: From Differential Equations to Diffusion Models | Diffusion models have emerged as a dominant framework for generative modeling, but their mathematical foundations are often presented separately through diffusion probabilistic models, score-based modeling, stochastic differential equations, and numerical sampling methods.
- [ ] relevant | `2605.30330v1` | When, why, and how do diffusion posterior samplers fail? A finite-sample lens | Diffusion models have excellent capacity to model complex distributions of natural data, which has made them a popular and effective choice for posterior sampling in imaging inverse problems.

## Q19

**Question:** Can the normally sequential denoising steps be computed concurrently by posing sampling as a fixed-point problem, and how many steps does that save?

**Gold:** `2402.09970v2` | Accelerating Parallel Sampling of Diffusion Models

> Diffusion models have emerged as state-of-the-art generative models for image generation. However, sampling from diffusion models is usually time-consuming due to the inherent autoregressive nature of their sampling process.

**Candidates:**

- [ ] relevant | `2110.05243v3` | Score-based diffusion models for accelerated MRI | Score-based diffusion models provide a powerful way to model images using the gradient of the data distribution.
- [ ] relevant | `2301.11558v1` | Accelerating Guided Diffusion Sampling with Splitting Numerical Methods | Guided diffusion is a technique for conditioning the output of a diffusion model at sampling time without retraining the network for each specific task.
- [ ] relevant | `2306.15512v1` | Trajectory Generation, Control, and Safety with Denoising Diffusion Probabilistic Models | We present a framework for safety-critical optimal control of physical systems based on denoising diffusion probabilistic models (DDPMs).
- [ ] relevant | `2311.10868v1` | SDDPM: Speckle Denoising Diffusion Probabilistic Models | Coherent imaging systems, such as medical ultrasound and synthetic aperture radar (SAR), are subject to corruption from speckle due to sub-resolution scatterers.
- [ ] relevant | `2401.08741v1` | Fixed Point Diffusion Models | We introduce the Fixed Point Diffusion Model (FPDM), a novel approach to image generation that integrates the concept of fixed point solving into the framework of diffusion-based generative modeling.
- [x] relevant (gold) | `2402.09970v2` | Accelerating Parallel Sampling of Diffusion Models | Diffusion models have emerged as state-of-the-art generative models for image generation.
- [ ] relevant | `2402.19455v2` | Listening to the Noise: Blind Denoising with Gibbs Diffusion | In recent years, denoising problems have become intertwined with the development of deep generative models.
- [ ] relevant | `2410.09945v2` | Variational Diffusion Posterior Sampling with Midpoint Guidance | Diffusion models have recently shown considerable potential in solving Bayesian inverse problems when used as priors.
- [ ] relevant | `2507.18654v2` | Diffusion Models for Solving Inverse Problems via Posterior Sampling with Piecewise Guidance | Diffusion models are powerful tools for sampling from high-dimensional distributions by progressively transforming pure noise into structured data through a denoising process.
- [ ] relevant | `2511.09180v1` | FSampler: Training Free Acceleration of Diffusion Sampling via Epsilon Extrapolation | FSampler is a training free, sampler agnostic execution layer that accelerates diffusion sampling by reducing the number of function evaluations (NFE).
- [ ] relevant | `2601.21868v2` | On Forgetting and Stability of Score-based Generative models | Understanding the stability and long-time behavior of generative models is a fundamental problem in modern machine learning.
- [ ] relevant | `2603.28572v1` | Unrestrained Simplex Denoising for Discrete Data. A Non-Markovian Approach Applied to Graph Generation | Denoising models such as Diffusion or Flow Matching have recently advanced generative modeling for discrete structures, yet most approaches either operate directly in the discrete state space, causing abrupt state changes.
- [ ] relevant | `2605.06831v2` | Why DDIM Hallucinates More Than DDPM: A Theoretical Analysis of Reverse Dynamics | We theoretically study the hallucination phenomena in two canonical diffusion samplers: the stochastic Denoising Diffusion Probabilistic Model (DDPM) and the deterministic Denoising Diffusion Implicit Model (DDIM).
- [ ] relevant | `2605.27990v1` | Geometry-Correct Diffusion Posterior Sampling with Denoiser-Pullback Curvature Guidance and Manifold-Aligned Damping | Diffusion posterior sampling conditions diffusion priors on measurements, but data-consistency updates are typically scaled by hand-tuned guidance weights and can destabilize sampling under stiff, operator-dependent curvature.

## Q20

**Question:** How can the spatial resolution of metabolic imaging of brain tumour patients be increased with a shortened diffusion chain?

**Gold:** `2410.19288v1` | A Flow-based Truncated Denoising Diffusion Model for Super-resolution Magnetic Resonance Spectroscopic Imaging

> Magnetic Resonance Spectroscopic Imaging (MRSI) is a non-invasive imaging technique for studying metabolism and has become a crucial tool for understanding neurological diseases, cancers and diabetes. High spatial resolution MRSI is needed to characterize lesions, but in practice MRSI is acquired at low resolution due to time and sensitivity restrictions caused by the low metabolite concentrations.

**Candidates:**

- [ ] relevant | `2110.05243v3` | Score-based diffusion models for accelerated MRI | Score-based diffusion models provide a powerful way to model images using the gradient of the data distribution.
- [ ] relevant | `2404.07724v2` | Applying Guidance in a Limited Interval Improves Sample and Distribution Quality in Diffusion Models | Guidance is a crucial technique for extracting the best performance out of image-generating diffusion models.
- [ ] relevant | `2405.12223v3` | Cascaded Multi-path Shortcut Diffusion Model for Medical Image Translation | Image-to-image translation is a vital component in medical imaging processing, with many uses in a wide range of imaging modalities and clinical scenarios.
- [ ] relevant | `2407.16477v2` | qMRI Diffuser: Quantitative T1 Mapping of the Brain using a Denoising Diffusion Probabilistic Model | Quantitative MRI (qMRI) offers significant advantages over weighted images by providing objective parameters related to tissue properties.
- [ ] relevant | `2410.11511v1` | Rician Denoising Diffusion Probabilistic Models For Sodium Breast MRI Enhancement | Sodium MRI is an imaging technique used to visualize and quantify sodium concentrations in vivo, playing a role in many biological processes and potentially aiding in breast cancer characterization.
- [x] relevant (gold) | `2410.19288v1` | A Flow-based Truncated Denoising Diffusion Model for Super-resolution Magnetic Resonance Spectroscopic Imaging | Magnetic Resonance Spectroscopic Imaging (MRSI) is a non-invasive imaging technique for studying metabolism and has become a crucial tool for understanding neurological diseases, cancers and diabetes.
- [ ] relevant | `2411.17203v1` | cWDM: Conditional Wavelet Diffusion Models for Cross-Modality 3D Medical Image Synthesis | This paper contributes to the "BraTS 2024 Brain MR Image Synthesis Challenge" and presents a conditional Wavelet Diffusion Model (cWDM) for directly solving a paired image-to-image translation task on high-resolution volumes.
- [ ] relevant | `2509.17790v1` | Conditional Diffusion Models for CT Image Synthesis from CBCT: A Systematic Review | Objective: Cone-beam computed tomography (CBCT) provides a low-dose imaging alternative to conventional CT, but suffers from noise, scatter, and artifacts that degrade image quality.
- [ ] relevant | `2510.17851v1` | Pre to Post-Treatment Glioblastoma MRI Prediction using a Latent Diffusion Model | Glioblastoma (GBM) is an aggressive primary brain tumor with a median survival of approximately 15 months.
- [ ] relevant | `2603.08709v1` | Scale Space Diffusion | Diffusion models degrade images through noise, and reversing this process reveals an information hierarchy across timesteps.
- [ ] relevant | `2605.27990v1` | Geometry-Correct Diffusion Posterior Sampling with Denoiser-Pullback Curvature Guidance and Manifold-Aligned Damping | Diffusion posterior sampling conditions diffusion priors on measurements, but data-consistency updates are typically scaled by hand-tuned guidance weights and can destabilize sampling under stiff, operator-dependent curvature.

## Q21

**Question:** How can block artefacts be avoided when a learned image codec encodes each patch independently, while still allowing patches to be decoded in parallel?

**Gold:** `1912.05189v2` | BINet: a binary inpainting network for deep patch-based image compression

> Recent deep learning models outperform standard lossy image compression codecs. However, applying these models on a patch-by-patch basis requires that each image patch be encoded and decoded independently.

**Candidates:**

- [x] relevant (gold) | `1912.05189v2` | BINet: a binary inpainting network for deep patch-based image compression | Recent deep learning models outperform standard lossy image compression codecs.
- [ ] relevant | `2006.11239v2` | Denoising Diffusion Probabilistic Models | We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.
- [ ] relevant | `2009.06912v1` | Learning a Single Model with a Wide Range of Quality Factors for JPEG Image Artifacts Removal | Lossy compression brings artifacts into the compressed image and degrades the visual quality.
- [ ] relevant | `2107.07675v1` | Beyond In-Place Corruption: Insertion and Deletion In Denoising Probabilistic Models | Denoising diffusion probabilistic models (DDPMs) have shown impressive results on sequence generation by iteratively corrupting each example and then learning to map corrupted versions back to the original.
- [ ] relevant | `2201.02625v3` | FlexHDR: Modelling Alignment and Exposure Uncertainties for Flexible HDR Imaging | High dynamic range (HDR) imaging is of fundamental importance in modern digital photography pipelines and used to produce a high-quality photograph with well exposed regions despite varying illumination across the image.
- [ ] relevant | `2201.09865v4` | RePaint: Inpainting using Denoising Diffusion Probabilistic Models | Free-form inpainting is the task of adding new content to an image in the regions specified by an arbitrary binary mask.
- [ ] relevant | `2301.06871v1` | Denoising Diffusion Probabilistic Models as a Defense against Adversarial Attacks | Neural Networks are infamously sensitive to small perturbations in their inputs, making them vulnerable to adversarial attacks.
- [ ] relevant | `2304.07087v1` | Memory Efficient Diffusion Probabilistic Models via Patch-based Generation | Diffusion probabilistic models have been successful in generating high-quality and diverse images.
- [ ] relevant | `2304.12526v2` | Patch Diffusion: Faster and More Data-Efficient Training of Diffusion Models | Diffusion models are powerful, but they require a lot of time and data to train.
- [ ] relevant | `2309.16106v2` | Neuromorphic Imaging with Joint Image Deblurring and Event Denoising | Neuromorphic imaging reacts to per-pixel brightness changes of a dynamic scene with high temporal precision and responds with asynchronous streaming events as a result.
- [ ] relevant | `2312.02156v2` | Latent Feature-Guided Diffusion Models for Shadow Removal | Recovering textures under shadows has remained a challenging problem due to the difficulty of inferring shadow-free scenes from shadow images.
- [ ] relevant | `2401.03221v1` | MirrorDiffusion: Stabilizing Diffusion Process in Zero-shot Image Translation by Prompts Redescription and Beyond | Recently, text-to-image diffusion models become a new paradigm in image processing fields, including content generation, image restoration and image-to-image translation.
- [ ] relevant | `2502.01522v2` | Unpaired Deblurring via Decoupled Diffusion Model | Generative diffusion models trained on large-scale datasets have achieved remarkable progress in image synthesis.
- [ ] relevant | `2506.06962v3` | AR-RAG: Autoregressive Retrieval Augmentation for Image Generation | We introduce Autoregressive Retrieval Augmentation (AR-RAG), a novel paradigm that enhances image generation by autoregressively incorporating knearest neighbor retrievals at the patch level.

## Q22

**Question:** How can an image generator look up reference patches repeatedly as it generates, instead of retrieving whole reference images once at the start?

**Gold:** `2506.06962v3` | AR-RAG: Autoregressive Retrieval Augmentation for Image Generation

> We introduce Autoregressive Retrieval Augmentation (AR-RAG), a novel paradigm that enhances image generation by autoregressively incorporating knearest neighbor retrievals at the patch level. Unlike prior methods that perform a single, static retrieval before generation and condition the entire generation on fixed reference images, AR-RAG performs context-aware retrievals at each generation step, using prior-generated patches as queries to retrieve and incorporate the most relevant patch-level visual references, enabling the model to respond to evolving generation needs while avoiding limitations (e.g., over-copying, stylistic bias, etc.) prevalent in existing methods.

**Candidates:**

- [ ] relevant | `1912.05189v2` | BINet: a binary inpainting network for deep patch-based image compression | Recent deep learning models outperform standard lossy image compression codecs.
- [ ] relevant | `2105.13695v1` | AutoSampling: Search for Effective Data Sampling Schedules | Data sampling acts as a pivotal role in training deep learning models.
- [ ] relevant | `2303.02490v2` | Diffusion Models Generate Images Like Painters: an Analytical Theory of Outline First, Details Later | How do diffusion generative models convert pure noise into meaningful images?
- [ ] relevant | `2303.09295v1` | DIRE for Diffusion-Generated Image Detection | Diffusion models have shown remarkable success in visual synthesis, but have also raised concerns about potential abuse for malicious purposes.
- [ ] relevant | `2304.07087v1` | Memory Efficient Diffusion Probabilistic Models via Patch-based Generation | Diffusion probabilistic models have been successful in generating high-quality and diverse images.
- [ ] relevant | `2304.12526v2` | Patch Diffusion: Faster and More Data-Efficient Training of Diffusion Models | Diffusion models are powerful, but they require a lot of time and data to train.
- [ ] relevant | `2401.03221v1` | MirrorDiffusion: Stabilizing Diffusion Process in Zero-shot Image Translation by Prompts Redescription and Beyond | Recently, text-to-image diffusion models become a new paradigm in image processing fields, including content generation, image restoration and image-to-image translation.
- [ ] relevant | `2401.08741v1` | Fixed Point Diffusion Models | We introduce the Fixed Point Diffusion Model (FPDM), a novel approach to image generation that integrates the concept of fixed point solving into the framework of diffusion-based generative modeling.
- [ ] relevant | `2402.09970v2` | Accelerating Parallel Sampling of Diffusion Models | Diffusion models have emerged as state-of-the-art generative models for image generation.
- [ ] relevant | `2406.01388v3` | AutoStudio: Crafting Consistent Subjects in Multi-turn Interactive Image Generation | As cutting-edge Text-to-Image (T2I) generation models already excel at producing remarkable single images, an even more challenging task, i.e., multi-turn interactive image generation begins to attract the attention of related research communities.
- [ ] relevant | `2411.15393v1` | Gradient-Free Classifier Guidance for Diffusion Model Sampling | Image generation using diffusion models have demonstrated outstanding learning capabilities, effectively capturing the full distribution of the training dataset.
- [ ] relevant | `2501.13926v2` | Can We Generate Images with CoT? Let's Verify and Reinforce Image Generation Step by Step | Chain-of-Thought (CoT) reasoning has been extensively explored in large models to tackle complex understanding tasks.
- [x] relevant (gold) | `2506.06962v3` | AR-RAG: Autoregressive Retrieval Augmentation for Image Generation | We introduce Autoregressive Retrieval Augmentation (AR-RAG), a novel paradigm that enhances image generation by autoregressively incorporating knearest neighbor retrievals at the patch level.
- [ ] relevant | `2506.10395v2` | Pisces: An Auto-regressive Foundation Model for Image Understanding and Generation | Recent advances in large language models (LLMs) have enabled multimodal foundation models to tackle both image understanding and generation within a unified framework.

## Q23

**Question:** How can linear dimensionality reduction for images be redesigned to keep what people perceive as image quality, instead of minimising pixel-by-pixel error?

**Gold:** `1908.09287v1` | Principal Component Analysis Using Structural Similarity Index for Images

> Despite the advances of deep learning in specific tasks using images, the principled assessment of image fidelity and similarity is still a critical ability to develop. As it has been shown that Mean Squared Error (MSE) is insufficient for this task, other measures have been developed with one of the most effective being Structural Similarity Index (SSIM).

**Candidates:**

- [x] relevant (gold) | `1908.09287v1` | Principal Component Analysis Using Structural Similarity Index for Images | Despite the advances of deep learning in specific tasks using images, the principled assessment of image fidelity and similarity is still a critical ability to develop.
- [ ] relevant | `1908.09288v1` | Locally Linear Image Structural Embedding for Image Structure Manifold Learning | Most of existing manifold learning methods rely on Mean Squared Error (MSE) or $\ell_2$ norm.
- [ ] relevant | `2303.02490v2` | Diffusion Models Generate Images Like Painters: an Analytical Theory of Outline First, Details Later | How do diffusion generative models convert pure noise into meaningful images?
- [ ] relevant | `2306.05720v2` | Beyond Surface Statistics: Scene Representations in a Latent Diffusion Model | Latent diffusion models (LDMs) exhibit an impressive ability to produce realistic images, yet the inner workings of these models remain mysterious.
- [ ] relevant | `2306.14891v2` | Fuzzy-Conditioned Diffusion and Diffusion Projection Attention Applied to Facial Image Correction | Image diffusion has recently shown remarkable performance in image synthesis and implicitly as an image prior.
- [ ] relevant | `2309.00885v1` | A Generic Fundus Image Enhancement Network Boosted by Frequency Self-supervised Representation Learning | Fundus photography is prone to suffer from image quality degradation that impacts clinical examination performed by ophthalmologists or intelligent systems.
- [ ] relevant | `2311.09952v1` | Score-based generative models learn manifold-like structures with constrained mixing | How do score-based generative models (SBMs) learn the data distribution supported on a low-dimensional manifold?
- [ ] relevant | `2311.10892v1` | The Hidden Linear Structure in Score-Based Models and its Application | Score-based models have achieved remarkable results in the generative modeling of many domains.
- [ ] relevant | `2312.04410v1` | Smooth Diffusion: Crafting Smooth Latent Spaces in Diffusion Models | Recently, diffusion models have made remarkable progress in text-to-image (T2I) generation, synthesizing images with high fidelity and diverse contents.
- [ ] relevant | `2405.15891v3` | Score Distillation via Reparametrized DDIM | While 2D diffusion models generate realistic, high-detail images, 3D shape generation methods like Score Distillation Sampling (SDS) built on these 2D diffusion models produce cartoon-like, over-smoothed shapes.
- [ ] relevant | `2407.07295v3` | Deformation-Recovery Diffusion Model (DRDM): Instance Deformation for Image Manipulation and Synthesis | In medical imaging, the diffusion models have shown great potential for synthetic image generation tasks.
- [ ] relevant | `2501.01423v3` | Reconstruction vs. Generation: Taming Optimization Dilemma in Latent Diffusion Models | Latent diffusion models with Transformer architectures excel at generating high-fidelity images.
- [ ] relevant | `2502.01522v2` | Unpaired Deblurring via Decoupled Diffusion Model | Generative diffusion models trained on large-scale datasets have achieved remarkable progress in image synthesis.
- [ ] relevant | `2503.01845v2` | Denoising Functional Maps: Diffusion Models for Shape Correspondence | Estimating correspondences between pairs of deformable shapes remains a challenging problem.
- [ ] relevant | `2603.08709v1` | Scale Space Diffusion | Diffusion models degrade images through noise, and reversing this process reveals an information hierarchy across timesteps.

## Q24

**Question:** When creating extra viewpoints from light-field camera data, why might it work better to measure training error on images combined from many views rather than on each view separately?

**Gold:** `1910.06072v5` | Light Field Synthesis by Training Deep Network in the Refocused Image Domain

> Light field imaging, which captures spatio-angular information of incident light on image sensor, enables many interesting applications like image refocusing and augmented reality. However, due to the limited sensor resolution, a trade-off exists between the spatial and angular resolution.

**Candidates:**

- [x] relevant (gold) | `1910.06072v5` | Light Field Synthesis by Training Deep Network in the Refocused Image Domain | Light field imaging, which captures spatio-angular information of incident light on image sensor, enables many interesting applications like image refocusing and augmented reality.
- [ ] relevant | `2107.14449v3` | Synth-by-Reg (SbR): Contrastive learning for synthesis-based registration of paired images | Nonlinear inter-modality registration is often challenging due to the lack of objective functions that are good proxies for alignment.
- [ ] relevant | `2201.00466v2` | RFormer: Transformer-based Generative Adversarial Network for Real Fundus Image Restoration on A New Clinical Benchmark | Ophthalmologists have used fundus images to screen and diagnose eye diseases.
- [ ] relevant | `2306.05720v2` | Beyond Surface Statistics: Scene Representations in a Latent Diffusion Model | Latent diffusion models (LDMs) exhibit an impressive ability to produce realistic images, yet the inner workings of these models remain mysterious.
- [ ] relevant | `2309.00885v1` | A Generic Fundus Image Enhancement Network Boosted by Frequency Self-supervised Representation Learning | Fundus photography is prone to suffer from image quality degradation that impacts clinical examination performed by ophthalmologists or intelligent systems.
- [ ] relevant | `2401.10227v2` | A Simple Latent Diffusion Approach for Panoptic Segmentation and Mask Inpainting | Panoptic and instance segmentation networks are often trained with specialized object detection modules, complex loss functions, and ad-hoc post-processing steps to manage the permutation-invariance of the instance masks.
- [ ] relevant | `2404.01709v1` | Upsample Guidance: Scale Up Diffusion Models without Training | Diffusion models have demonstrated superior performance across various generative tasks including images, videos, and audio.
- [ ] relevant | `2407.07295v3` | Deformation-Recovery Diffusion Model (DRDM): Instance Deformation for Image Manipulation and Synthesis | In medical imaging, the diffusion models have shown great potential for synthetic image generation tasks.
- [ ] relevant | `2409.19365v3` | Conditional Image Synthesis with Diffusion Models: A Survey | Conditional image synthesis based on user-specified requirements is a key component in creating complex visual content.
- [ ] relevant | `2410.02416v2` | Eliminating Oversaturation and Artifacts of High Guidance Scales in Diffusion Models | Classifier-free guidance (CFG) is crucial for improving both generation quality and alignment between the input condition and final output in diffusion models.
- [ ] relevant | `2412.06029v1` | Latent-Reframe: Enabling Camera Control for Video Diffusion Model without Training | Precise camera pose control is crucial for video generation with diffusion models.
- [ ] relevant | `2412.09966v1` | EP-CFG: Energy-Preserving Classifier-Free Guidance | Classifier-free guidance (CFG) is widely used in diffusion models but often introduces over-contrast and over-saturation artifacts at higher guidance strengths.
- [ ] relevant | `2508.10688v2` | Novel View Synthesis using DDIM Inversion | Synthesizing novel views from a single input image is a challenging task.
- [ ] relevant | `2511.05844v3` | Enhancing Diffusion Model Guidance through Calibration and Regularization | Classifier-guided diffusion models have emerged as a powerful approach for conditional image generation, but they suffer from overconfident predictions during early denoising steps, causing the guidance gradient to vanish.
- [ ] relevant | `2606.09828v1` | Latent Spatial Memory for Video World Models | Video world models that maintain 3D spatial consistency across generated frames typically rely on explicit point cloud memory constructed in RGB space.

## Q25

**Question:** How can a diffusion-based method remove blur from images when no matched sharp and blurry training pairs exist for the target domain?

**Gold:** `2502.01522v2` | Unpaired Deblurring via Decoupled Diffusion Model

> Generative diffusion models trained on large-scale datasets have achieved remarkable progress in image synthesis. In favor of their ability to supplement missing details and generate aesthetically pleasing contents, recent works have applied them to image deblurring via training an adapter on blurry-sharp image pairs to provide structural conditions for restoration.

**Candidates:**

- [ ] relevant | `2006.11239v2` | Denoising Diffusion Probabilistic Models | We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.
- [ ] relevant | `2104.05358v1` | UNIT-DDPM: UNpaired Image Translation with Denoising Diffusion Probabilistic Models | We propose a novel unpaired image-to-image translation method that uses denoising diffusion probabilistic models without requiring adversarial training.
- [ ] relevant | `2110.05243v3` | Score-based diffusion models for accelerated MRI | Score-based diffusion models provide a powerful way to model images using the gradient of the data distribution.
- [ ] relevant | `2201.09865v4` | RePaint: Inpainting using Denoising Diffusion Probabilistic Models | Free-form inpainting is the task of adding new content to an image in the regions specified by an arbitrary binary mask.
- [ ] relevant | `2207.12598v1` | Classifier-Free Diffusion Guidance | Classifier guidance is a recently introduced method to trade off mode coverage and sample fidelity in conditional diffusion models post training, in the same spirit as low temperature sampling or truncation in other types of generative models.
- [ ] relevant | `2210.00939v6` | Improving Sample Quality of Diffusion Models Using Self-Attention Guidance | Denoising diffusion models (DDMs) have attracted attention for their exceptional generation quality and diversity.
- [ ] relevant | `2301.11558v1` | Accelerating Guided Diffusion Sampling with Splitting Numerical Methods | Guided diffusion is a technique for conditioning the output of a diffusion model at sampling time without retraining the network for each specific task.
- [ ] relevant | `2306.14891v2` | Fuzzy-Conditioned Diffusion and Diffusion Projection Attention Applied to Facial Image Correction | Image diffusion has recently shown remarkable performance in image synthesis and implicitly as an image prior.
- [ ] relevant | `2312.02156v2` | Latent Feature-Guided Diffusion Models for Shadow Removal | Recovering textures under shadows has remained a challenging problem due to the difficulty of inferring shadow-free scenes from shadow images.
- [ ] relevant | `2312.07586v5` | Characteristic Guidance: Non-linear Correction for Diffusion Model at Large Guidance Scale | Popular guidance for denoising diffusion probabilistic model (DDPM) linearly combines distinct conditional models together to provide enhanced control over samples.
- [ ] relevant | `2401.03221v1` | MirrorDiffusion: Stabilizing Diffusion Process in Zero-shot Image Translation by Prompts Redescription and Beyond | Recently, text-to-image diffusion models become a new paradigm in image processing fields, including content generation, image restoration and image-to-image translation.
- [ ] relevant | `2401.05779v4` | Erasing Undesirable Influence in Diffusion Models | Diffusion models are highly effective at generating high-quality images but pose risks, such as the unintentional generation of NSFW (not safe for work) content.
- [ ] relevant | `2409.19365v3` | Conditional Image Synthesis with Diffusion Models: A Survey | Conditional image synthesis based on user-specified requirements is a key component in creating complex visual content.
- [ ] relevant | `2412.09966v1` | EP-CFG: Energy-Preserving Classifier-Free Guidance | Classifier-free guidance (CFG) is widely used in diffusion models but often introduces over-contrast and over-saturation artifacts at higher guidance strengths.
- [x] relevant (gold) | `2502.01522v2` | Unpaired Deblurring via Decoupled Diffusion Model | Generative diffusion models trained on large-scale datasets have achieved remarkable progress in image synthesis.
- [ ] relevant | `2503.08434v5` | Bokeh Diffusion: Defocus Blur Control in Text-to-Image Diffusion Models | Recent advances in large-scale text-to-image models have revolutionized creative fields by generating visually captivating outputs from textual prompts; however, while traditional photography offers precise control over camera settings to shape visual aesthetics - such as depth-of-field via aperture - current diffusion models typically rely on prompt engineering to mimic such effects.

## Q26

**Question:** Reconstruction quality drops at large guidance scales when real photos are edited by inverting a deterministic sampler; how can a training-free negative-prompt approach be improved to reduce the resulting artifacts?

**Gold:** `2306.05414v3` | Improving Tuning-Free Real Image Editing with Proximal Guidance

> DDIM inversion has revealed the remarkable potential of real image editing within diffusion-based methods. However, the accuracy of DDIM reconstruction degrades as larger classifier-free guidance (CFG) scales being used for enhanced editing.

**Candidates:**

- [x] relevant (gold) | `2306.05414v3` | Improving Tuning-Free Real Image Editing with Proximal Guidance | DDIM inversion has revealed the remarkable potential of real image editing within diffusion-based methods.
- [ ] relevant | `2307.02814v1` | Single Image LDR to HDR Conversion using Conditional Diffusion | Digital imaging aims to replicate realistic scenes, but Low Dynamic Range (LDR) cameras cannot represent the wide dynamic range of real scenes, resulting in under-/overexposed images.
- [ ] relevant | `2312.07586v5` | Characteristic Guidance: Non-linear Correction for Diffusion Model at Large Guidance Scale | Popular guidance for denoising diffusion probabilistic model (DDPM) linearly combines distinct conditional models together to provide enhanced control over samples.
- [ ] relevant | `2312.08195v2` | Image is All You Need to Empower Large-scale Diffusion Models for In-Domain Generation | In-domain generation aims to perform a variety of tasks within a specific domain, such as unconditional generation, text-to-image, image editing, 3D generation, and more.
- [ ] relevant | `2401.03221v1` | MirrorDiffusion: Stabilizing Diffusion Process in Zero-shot Image Translation by Prompts Redescription and Beyond | Recently, text-to-image diffusion models become a new paradigm in image processing fields, including content generation, image restoration and image-to-image translation.
- [ ] relevant | `2403.17377v2` | Self-Rectifying Diffusion Sampling with Perturbed-Attention Guidance | Recent studies have demonstrated that diffusion models are capable of generating high-quality samples, but their quality heavily depends on sampling guidance techniques, such as classifier guidance (CG) and classifier-free guidance (CFG).
- [ ] relevant | `2404.01709v1` | Upsample Guidance: Scale Up Diffusion Models without Training | Diffusion models have demonstrated superior performance across various generative tasks including images, videos, and audio.
- [ ] relevant | `2404.07724v2` | Applying Guidance in a Limited Interval Improves Sample and Distribution Quality in Diffusion Models | Guidance is a crucial technique for extracting the best performance out of image-generating diffusion models.
- [ ] relevant | `2409.19365v3` | Conditional Image Synthesis with Diffusion Models: A Survey | Conditional image synthesis based on user-specified requirements is a key component in creating complex visual content.
- [ ] relevant | `2410.02416v2` | Eliminating Oversaturation and Artifacts of High Guidance Scales in Diffusion Models | Classifier-free guidance (CFG) is crucial for improving both generation quality and alignment between the input condition and final output in diffusion models.
- [ ] relevant | `2411.18664v1` | Spatiotemporal Skip Guidance for Enhanced Video Diffusion Sampling | Diffusion models have emerged as a powerful tool for generating high-quality images, videos, and 3D content.
- [ ] relevant | `2412.09966v1` | EP-CFG: Energy-Preserving Classifier-Free Guidance | Classifier-free guidance (CFG) is widely used in diffusion models but often introduces over-contrast and over-saturation artifacts at higher guidance strengths.
- [ ] relevant | `2505.09571v1` | Don't Forget your Inverse DDIM for Image Editing | The field of text-to-image generation has undergone significant advancements with the introduction of diffusion models.
- [ ] relevant | `2507.18654v2` | Diffusion Models for Solving Inverse Problems via Posterior Sampling with Piecewise Guidance | Diffusion models are powerful tools for sampling from high-dimensional distributions by progressively transforming pure noise into structured data through a denoising process.
- [ ] relevant | `2511.05844v3` | Enhancing Diffusion Model Guidance through Calibration and Regularization | Classifier-guided diffusion models have emerged as a powerful approach for conditional image generation, but they suffer from overconfident predictions during early denoising steps, causing the guidance gradient to vanish.

## Q27

**Question:** How can several diffusion models be combined at test time so that a generated image correctly binds attributes to objects and respects the relations in a complex prompt?

**Gold:** `2206.01714v6` | Compositional Visual Generation with Composable Diffusion Models

> Large text-guided diffusion models, such as DALLE-2, are able to generate stunning photorealistic images given natural language descriptions. While such models are highly flexible, they struggle to understand the composition of certain concepts, such as confusing the attributes of different objects or relations between objects.

**Candidates:**

- [ ] relevant | `2111.13606v1` | Conditional Image Generation with Score-Based Diffusion Models | Score-based diffusion models have emerged as one of the most promising frameworks for deep generative modelling.
- [x] relevant (gold) | `2206.01714v6` | Compositional Visual Generation with Composable Diffusion Models | Large text-guided diffusion models, such as DALLE-2, are able to generate stunning photorealistic images given natural language descriptions.
- [ ] relevant | `2207.12598v1` | Classifier-Free Diffusion Guidance | Classifier guidance is a recently introduced method to trade off mode coverage and sample fidelity in conditional diffusion models post training, in the same spirit as low temperature sampling or truncation in other types of generative models.
- [ ] relevant | `2212.04488v2` | Multi-Concept Customization of Text-to-Image Diffusion | While generative models produce high-quality images of concepts learned from a large-scale database, a user often wishes to synthesize instantiations of their own concepts (for example, their family, pets, or items).
- [ ] relevant | `2303.02490v2` | Diffusion Models Generate Images Like Painters: an Analytical Theory of Outline First, Details Later | How do diffusion generative models convert pure noise into meaningful images?
- [ ] relevant | `2303.09295v1` | DIRE for Diffusion-Generated Image Detection | Diffusion models have shown remarkable success in visual synthesis, but have also raised concerns about potential abuse for malicious purposes.
- [ ] relevant | `2305.16223v2` | Prompt-Free Diffusion: Taking "Text" out of Text-to-Image Diffusion Models | Text-to-image (T2I) research has grown explosively in the past year, owing to the large-scale pre-trained diffusion models and many emerging personalization and editing approaches.
- [ ] relevant | `2311.10892v1` | The Hidden Linear Structure in Score-Based Models and its Application | Score-based models have achieved remarkable results in the generative modeling of many domains.
- [ ] relevant | `2312.07586v5` | Characteristic Guidance: Non-linear Correction for Diffusion Model at Large Guidance Scale | Popular guidance for denoising diffusion probabilistic model (DDPM) linearly combines distinct conditional models together to provide enhanced control over samples.
- [ ] relevant | `2402.13144v3` | Neural Network Diffusion | Diffusion models have achieved remarkable success in image and video generation.
- [ ] relevant | `2403.04279v2` | Controllable Generation with Text-to-Image Diffusion Models: A Survey | In the rapidly advancing realm of visual generation, diffusion models have revolutionized the landscape, marking a significant shift in capabilities with their impressive text-guided generative functions.
- [ ] relevant | `2404.07724v2` | Applying Guidance in a Limited Interval Improves Sample and Distribution Quality in Diffusion Models | Guidance is a crucial technique for extracting the best performance out of image-generating diffusion models.
- [ ] relevant | `2409.19365v3` | Conditional Image Synthesis with Diffusion Models: A Survey | Conditional image synthesis based on user-specified requirements is a key component in creating complex visual content.
- [ ] relevant | `2504.16080v1` | From Reflection to Perfection: Scaling Inference-Time Optimization for Text-to-Image Diffusion Models via Reflection Tuning | Recent text-to-image diffusion models achieve impressive visual quality through extensive scaling of training data and model parameters, yet they often struggle with complex scenes and fine-grained details.
- [ ] relevant | `2510.11057v1` | Temporal Alignment Guidance: On-Manifold Sampling in Diffusion Models | Diffusion models have achieved remarkable success as generative models.
- [ ] relevant | `2603.29239v1` | Diffusion Mental Averages | Can a diffusion model produce its own "mental average" of a concept-one that is as sharp and realistic as a typical sample?

## Q28

**Question:** How can a text prompt be turned into an animatable 3D face by optimising a parametric head model with a 2D image diffusion prior?

**Gold:** `2307.04859v1` | Articulated 3D Head Avatar Generation using Text-to-Image Diffusion Models

> The ability to generate diverse 3D articulated head avatars is vital to a plethora of applications, including augmented reality, cinematography, and education. Recent work on text-guided 3D object generation has shown great promise in addressing these needs.

**Candidates:**

- [ ] relevant | `2302.08510v2` | Text-driven Visual Synthesis with Latent Diffusion Prior | There has been tremendous progress in large-scale text-to-image synthesis driven by diffusion models enabling versatile downstream applications such as 3D object synthesis from texts, image editing, and customized generation.
- [ ] relevant | `2303.04291v2` | Diffusion in the Dark: A Diffusion Model for Low-Light Text Recognition | Capturing images is a key part of automation for high-level tasks such as scene text recognition.
- [ ] relevant | `2303.07909v3` | Text-to-image Diffusion Models in Generative AI: A Survey | This survey reviews the progress of diffusion models in generating images from text, ~\textit{i.e.} text-to-image diffusion models.
- [ ] relevant | `2305.16223v2` | Prompt-Free Diffusion: Taking "Text" out of Text-to-Image Diffusion Models | Text-to-image (T2I) research has grown explosively in the past year, owing to the large-scale pre-trained diffusion models and many emerging personalization and editing approaches.
- [x] relevant (gold) | `2307.04859v1` | Articulated 3D Head Avatar Generation using Text-to-Image Diffusion Models | The ability to generate diverse 3D articulated head avatars is vital to a plethora of applications, including augmented reality, cinematography, and education.
- [ ] relevant | `2311.03226v1` | LDM3D-VR: Latent Diffusion Model for 3D VR | Latent diffusion models have proven to be state-of-the-art in the creation and manipulation of visual outputs.
- [ ] relevant | `2401.03221v1` | MirrorDiffusion: Stabilizing Diffusion Process in Zero-shot Image Translation by Prompts Redescription and Beyond | Recently, text-to-image diffusion models become a new paradigm in image processing fields, including content generation, image restoration and image-to-image translation.
- [ ] relevant | `2403.04279v2` | Controllable Generation with Text-to-Image Diffusion Models: A Survey | In the rapidly advancing realm of visual generation, diffusion models have revolutionized the landscape, marking a significant shift in capabilities with their impressive text-guided generative functions.
- [ ] relevant | `2406.14555v1` | A Survey of Multimodal-Guided Image Editing with Text-to-Image Diffusion Models | Image editing aims to edit the given synthetic or real image to meet the specific requirements from users.
- [ ] relevant | `2407.04800v1` | Segmentation-Free Guidance for Text-to-Image Diffusion Models | We introduce segmentation-free guidance, a novel method designed for text-to-image diffusion models like Stable Diffusion.
- [ ] relevant | `2409.03718v1` | Geometry Image Diffusion: Fast and Data-Efficient Text-to-3D with Image-Based Surface Representation | Generating high-quality 3D objects from textual descriptions remains a challenging problem due to computational cost, the scarcity of 3D data, and complex 3D representations.
- [ ] relevant | `2503.08434v5` | Bokeh Diffusion: Defocus Blur Control in Text-to-Image Diffusion Models | Recent advances in large-scale text-to-image models have revolutionized creative fields by generating visually captivating outputs from textual prompts; however, while traditional photography offers precise control over camera settings to shape visual aesthetics - such as depth-of-field via aperture - current diffusion models typically rely on prompt engineering to mimic such effects.
- [ ] relevant | `2506.08351v1` | How Much To Guide: Revisiting Adaptive Guidance in Classifier-Free Guidance Text-to-Vision Diffusion Models | With the rapid development of text-to-vision generation diffusion models, classifier-free guidance has emerged as the most prevalent method for conditioning.
- [ ] relevant | `2506.24108v3` | Navigating with Annealing Guidance Scale in Diffusion Space | Denoising diffusion models excel at generating high-quality images conditioned on text prompts, yet their effectiveness heavily relies on careful guidance during the sampling process.
- [ ] relevant | `2508.21032v1` | Reusing Computation in Text-to-Image Diffusion for Efficient Generation of Image Sets | Text-to-image diffusion models enable high-quality image generation but are computationally expensive.

## Q29

**Question:** How can people's judgments of generated images be turned into tokens that help remove harmful or copyrighted concepts from an image generator?

**Gold:** `2407.21032v1` | Safeguard Text-to-Image Diffusion Models with Human Feedback Inversion

> This paper addresses the societal concerns arising from large-scale text-to-image diffusion models for generating potentially harmful or copyrighted content. Existing models rely heavily on internet-crawled data, wherein problematic concepts persist due to incomplete filtration processes.

**Candidates:**

- [ ] relevant | `2206.01714v6` | Compositional Visual Generation with Composable Diffusion Models | Large text-guided diffusion models, such as DALLE-2, are able to generate stunning photorealistic images given natural language descriptions.
- [ ] relevant | `2303.09295v1` | DIRE for Diffusion-Generated Image Detection | Diffusion models have shown remarkable success in visual synthesis, but have also raised concerns about potential abuse for malicious purposes.
- [ ] relevant | `2305.16223v2` | Prompt-Free Diffusion: Taking "Text" out of Text-to-Image Diffusion Models | Text-to-image (T2I) research has grown explosively in the past year, owing to the large-scale pre-trained diffusion models and many emerging personalization and editing approaches.
- [ ] relevant | `2307.08025v1` | Analysing Gender Bias in Text-to-Image Models using Object Detection | This work presents a novel strategy to measure bias in text-to-image models.
- [ ] relevant | `2311.13619v1` | Steal My Artworks for Fine-tuning? A Watermarking Framework for Detecting Art Theft Mimicry in Text-to-Image Models | The advancement in text-to-image models has led to astonishing artistic performances.
- [ ] relevant | `2404.06666v3` | SafeGen: Mitigating Sexually Explicit Content Generation in Text-to-Image Models | Text-to-image (T2I) models, such as Stable Diffusion, have exhibited remarkable performance in generating high-quality images from text descriptions in recent years.
- [x] relevant (gold) | `2407.21032v1` | Safeguard Text-to-Image Diffusion Models with Human Feedback Inversion | This paper addresses the societal concerns arising from large-scale text-to-image diffusion models for generating potentially harmful or copyrighted content.
- [ ] relevant | `2411.05706v1` | Image2Text2Image: A Novel Framework for Label-Free Evaluation of Image-to-Text Generation with Text-to-Image Diffusion Models | Evaluating the quality of automatically generated image descriptions is a complex task that requires metrics capturing various dimensions, such as grammaticality, coverage, accuracy, and truthfulness.
- [ ] relevant | `2411.16738v2` | Classifier-Free Guidance inside the Attraction Basin May Cause Memorization | Diffusion models are prone to exactly reproduce images from the training data.
- [ ] relevant | `2412.07229v2` | Moderating the Generalization of Score-based Generative Model | Score-based Generative Models (SGMs) have demonstrated remarkable generalization abilities, e.g. generating unseen, but natural data.
- [ ] relevant | `2412.20800v1` | VMix: Improving Text-to-Image Diffusion Model with Cross-Attention Mixing Control | While diffusion models show extraordinary talents in text-to-image generation, they may still fail to generate highly aesthetic images.
- [ ] relevant | `2501.13926v2` | Can We Generate Images with CoT? Let's Verify and Reinforce Image Generation Step by Step | Chain-of-Thought (CoT) reasoning has been extensively explored in large models to tackle complex understanding tasks.
- [ ] relevant | `2606.13247v1` | EPIG: Emotion-Based Prompting for Personalised Image Generation | Text-to-image diffusion models have achieved impressive results in synthesizing high-quality images from natural language prompts.

## Q30

**Question:** How can the number of points or strokes in generated free-hand drawings be controlled explicitly?

**Gold:** `2306.09274v1` | Conditional Human Sketch Synthesis with Explicit Abstraction Control

> This paper presents a novel free-hand sketch synthesis approach addressing explicit abstraction control in class-conditional and photo-to-sketch synthesis. Abstraction is a vital aspect of sketches, as it defines the fundamental distinction between a sketch and an image.

**Candidates:**

- [ ] relevant | `2110.15678v3` | A Shading-Guided Generative Implicit Model for Shape-Accurate 3D-Aware Image Synthesis | The advancement of generative radiance fields has pushed the boundary of 3D-aware image synthesis.
- [ ] relevant | `2302.04411v1` | Geometry of Score Based Generative Models | In this work, we look at Score-based generative models (also called diffusion generative models) from a geometric perspective.
- [ ] relevant | `2303.02490v2` | Diffusion Models Generate Images Like Painters: an Analytical Theory of Outline First, Details Later | How do diffusion generative models convert pure noise into meaningful images?
- [ ] relevant | `2304.03373v2` | Training-Free Layout Control with Cross-Attention Guidance | Recent diffusion-based generators can produce high-quality images from textual prompts.
- [x] relevant (gold) | `2306.09274v1` | Conditional Human Sketch Synthesis with Explicit Abstraction Control | This paper presents a novel free-hand sketch synthesis approach addressing explicit abstraction control in class-conditional and photo-to-sketch synthesis.
- [ ] relevant | `2307.04859v1` | Articulated 3D Head Avatar Generation using Text-to-Image Diffusion Models | The ability to generate diverse 3D articulated head avatars is vital to a plethora of applications, including augmented reality, cinematography, and education.
- [ ] relevant | `2312.08195v2` | Image is All You Need to Empower Large-scale Diffusion Models for In-Domain Generation | In-domain generation aims to perform a variety of tasks within a specific domain, such as unconditional generation, text-to-image, image editing, 3D generation, and more.
- [ ] relevant | `2403.04279v2` | Controllable Generation with Text-to-Image Diffusion Models: A Survey | In the rapidly advancing realm of visual generation, diffusion models have revolutionized the landscape, marking a significant shift in capabilities with their impressive text-guided generative functions.
- [ ] relevant | `2409.03718v1` | Geometry Image Diffusion: Fast and Data-Efficient Text-to-3D with Image-Based Surface Representation | Generating high-quality 3D objects from textual descriptions remains a challenging problem due to computational cost, the scarcity of 3D data, and complex 3D representations.
- [ ] relevant | `2501.13926v2` | Can We Generate Images with CoT? Let's Verify and Reinforce Image Generation Step by Step | Chain-of-Thought (CoT) reasoning has been extensively explored in large models to tackle complex understanding tasks.
- [ ] relevant | `2503.21943v2` | Parametric Shadow Control for Portrait Generation in Text-to-Image Diffusion Models | Text-to-image diffusion models excel at generating diverse portraits, but lack intuitive shadow control.
- [ ] relevant | `2504.20754v1` | DDPS: Discrete Diffusion Posterior Sampling for Paths in Layered Graphs | Diffusion models form an important class of generative models today, accounting for much of the state of the art in cutting edge AI research.
- [ ] relevant | `2510.16223v1` | Case Study of GAI for Generating Novel Images for Real-World Embroidery | In this paper, we present a case study exploring the potential use of Generative Artificial Intelligence (GAI) to address the real-world need of making the design of embroiderable art patterns more accessible.

## Q31

**Question:** How can a large language model be made to forget information without a dataset of knowledge to keep, with guidance applied at inference?

**Gold:** `2412.06846v1` | Classifier-free guidance in LLMs Safety

> The paper describes LLM unlearning without a retaining dataset, using the ORPO reinforcement learning method with inference enhanced by modified classifier-free guidance. Significant improvement in unlearning, without degradation of the model, is achieved through direct training on synthetic replacement data in CFG-aware training regime, with classifier-free guidance applied during the inference.

**Candidates:**

- [ ] relevant | `2212.11685v2` | Text Generation with Diffusion Language Models: A Pre-training Approach with Continuous Paragraph Denoise | In this paper, we introduce a novel dIffusion language modEl pre-training framework for text generation, which we call GENIE.
- [ ] relevant | `2302.00860v3` | Modeling Causal Mechanisms with Diffusion Models for Interventional and Counterfactual Queries | We consider the problem of answering observational, interventional, and counterfactual queries in a causally sufficient setting where only observational data and the causal graph are available.
- [ ] relevant | `2310.05264v5` | The Emergence of Reproducibility and Generalizability in Diffusion Models | In this work, we investigate an intriguing and prevalent phenomenon of diffusion models which we term as "consistent model reproducibility": given the same starting noise input and a deterministic sampler, different diffusion models often yield remarkably similar outputs.
- [ ] relevant | `2312.08195v2` | Image is All You Need to Empower Large-scale Diffusion Models for In-Domain Generation | In-domain generation aims to perform a variety of tasks within a specific domain, such as unconditional generation, text-to-image, image editing, 3D generation, and more.
- [ ] relevant | `2411.16738v2` | Classifier-Free Guidance inside the Attraction Basin May Cause Memorization | Diffusion models are prone to exactly reproduce images from the training data.
- [x] relevant (gold) | `2412.06846v1` | Classifier-free guidance in LLMs Safety | The paper describes LLM unlearning without a retaining dataset, using the ORPO reinforcement learning method with inference enhanced by modified classifier-free guidance.
- [ ] relevant | `2503.10638v3` | Studying Classifier(-Free) Guidance From a Classifier-Centric Perspective | Classifier-free guidance has become a staple for conditional generation with denoising diffusion models.
- [ ] relevant | `2505.20199v1` | Adaptive Classifier-Free Guidance via Dynamic Low-Confidence Masking | Classifier-Free Guidance (CFG) significantly enhances controllability in generative models by interpolating conditional and unconditional predictions.
- [ ] relevant | `2506.14399v5` | Factored Classifier-Free Guidance | Counterfactual generation aims to simulate realistic hypothetical outcomes under causal interventions.
- [ ] relevant | `2509.22007v2` | Stage-wise Dynamics of Classifier-Free Guidance in Diffusion Models | Classifier-Free Guidance (CFG) is widely used to improve conditional fidelity in diffusion models, but its impact on sampling dynamics remains poorly understood.
- [ ] relevant | `2509.22728v2` | Prompt-aware classifier free guidance for diffusion models | Diffusion models have achieved remarkable progress in image and audio generation, largely due to Classifier-Free Guidance.
- [ ] relevant | `2512.17303v1` | EMAG: Self-Rectifying Diffusion Sampling with Exponential Moving Average Guidance | In diffusion and flow-matching generative models, guidance techniques are widely used to improve sample quality and consistency.
- [ ] relevant | `2601.21868v2` | On Forgetting and Stability of Score-based Generative models | Understanding the stability and long-time behavior of generative models is a fundamental problem in modern machine learning.
- [ ] relevant | `2602.07546v1` | Improving Variable-Length Generation in Diffusion Language Models via Length Regularization | Diffusion Large Language Models (DLLMs) are inherently ill-suited for variable-length generation, as their inference is defined on a fixed-length canvas and implicitly assumes a known target length.
- [ ] relevant | `2606.16360v1` | Tyler: Typed Latent Reasoning for Language Models -- When to Think, What to Compute, and How Much to Allocate | Chain-of-thought (CoT) prompting improves reasoning in large language models (LLMs) by externalizing intermediate computation as discrete text tokens, but this textual interface also introduces redundancy and inference overhead.

## Q32

**Question:** In a masked diffusion language model, how can the unconditional branch of guidance be built dynamically from the tokens the model is least sure about?

**Gold:** `2505.20199v1` | Adaptive Classifier-Free Guidance via Dynamic Low-Confidence Masking

> Classifier-Free Guidance (CFG) significantly enhances controllability in generative models by interpolating conditional and unconditional predictions. However, standard CFG often employs a static unconditional input, which can be suboptimal for iterative generation processes where model uncertainty varies dynamically.

**Candidates:**

- [ ] relevant | `2207.12598v1` | Classifier-Free Diffusion Guidance | Classifier guidance is a recently introduced method to trade off mode coverage and sample fidelity in conditional diffusion models post training, in the same spirit as low temperature sampling or truncation in other types of generative models.
- [ ] relevant | `2304.04746v1` | A Cheaper and Better Diffusion Language Model with Soft-Masked Noise | Diffusion models that are based on iterative denoising have been recently proposed and leveraged in various generation tasks like image generation.
- [ ] relevant | `2311.00938v1` | Bridging the Gap: Addressing Discrepancies in Diffusion Model Training for Classifier-Free Guidance | Diffusion models have emerged as a pivotal advancement in generative models, setting new standards to the quality of the generated instances.
- [ ] relevant | `2407.02687v2` | No Training, No Problem: Rethinking Classifier-Free Guidance for Diffusion Models | Classifier-free guidance (CFG) has become the standard method for enhancing the quality of conditional diffusion models.
- [ ] relevant | `2408.09000v2` | Classifier-Free Guidance is a Predictor-Corrector | We investigate the theoretical foundations of classifier-free guidance (CFG).
- [x] relevant (gold) | `2505.20199v1` | Adaptive Classifier-Free Guidance via Dynamic Low-Confidence Masking | Classifier-Free Guidance (CFG) significantly enhances controllability in generative models by interpolating conditional and unconditional predictions.
- [ ] relevant | `2505.21101v1` | Conditional Diffusion Models with Classifier-Free Gibbs-like Guidance | Classifier-Free Guidance (CFG) is a widely used technique for improving conditional diffusion models by linearly combining the outputs of conditional and unconditional denoisers.
- [ ] relevant | `2506.10036v2` | Token Perturbation Guidance for Diffusion Models | Classifier-free guidance (CFG) has become an essential component of modern diffusion models to enhance both generation quality and alignment with input conditions.
- [ ] relevant | `2506.21452v1` | Rethinking Oversaturation in Classifier-Free Guidance via Low Frequency | Classifier-free guidance (CFG) succeeds in condition diffusion models that use a guidance scale to balance the influence of conditional and unconditional terms.
- [ ] relevant | `2507.08965v2` | Improving Classifier-Free Guidance in Masked Diffusion: Low-Dim Theoretical Insights with High-Dim Impact | Classifier-Free Guidance (CFG) is a widely used technique for conditional generation and improving sample quality in continuous diffusion models, and its extensions to discrete diffusion has recently started to be investigated.
- [ ] relevant | `2509.22007v2` | Stage-wise Dynamics of Classifier-Free Guidance in Diffusion Models | Classifier-Free Guidance (CFG) is widely used to improve conditional fidelity in diffusion models, but its impact on sampling dynamics remains poorly understood.
- [ ] relevant | `2602.07546v1` | Improving Variable-Length Generation in Diffusion Language Models via Length Regularization | Diffusion Large Language Models (DLLMs) are inherently ill-suited for variable-length generation, as their inference is defined on a fixed-length canvas and implicitly assumes a known target length.
- [ ] relevant | `2603.08155v3` | C$^2$FG: Control Classifier-Free Guidance via Score Discrepancy Analysis | Classifier-Free Guidance (CFG) is a cornerstone of modern conditional diffusion models, yet its reliance on the fixed or heuristic dynamic guidance weight is predominantly empirical and overlooks the inherent dynamics of the diffusion process.

## Q33

**Question:** How can a decision tree be grown when the data are grouped by a control variable, such as sex or time, that may confound the outcome?

**Gold:** `2606.13295v2` | Simultaneous Latent Budget Trees for Stratified Classification

> In the era of Explainable Artificial Intelligence, there is a renewed focus on single trees for their ease of interpretation. This paper introduces Simultaneous Latent Budget Trees, a probabilistic machine learning framework for classification trees in the presence of a stratification factor such as a temporal, spatial, or demographic variable, acting as a control variable or potential confounder.

**Candidates:**

- [ ] relevant | `0405062v1` | Efficiency Enhancement of Probabilistic Model Building Genetic Algorithms | This paper presents two different efficiency-enhancement techniques for probabilistic model building genetic algorithms.
- [ ] relevant | `2001.04197v4` | Causal discovery of linear non-Gaussian acyclic models in the presence of latent confounders | Causal discovery from data affected by latent confounders is an important and difficult challenge.
- [ ] relevant | `2307.08025v1` | Analysing Gender Bias in Text-to-Image Models using Object Detection | This work presents a novel strategy to measure bias in text-to-image models.
- [ ] relevant | `2312.02246v4` | Conditional Variational Diffusion Models | Inverse problems aim to determine parameters from observations, a crucial task in engineering and science.
- [ ] relevant | `2412.10193v3` | Simple Guidance Mechanisms for Discrete Diffusion Models | Diffusion models for continuous data gained widespread adoption owing to their high quality generation and control mechanisms.
- [ ] relevant | `2502.17100v4` | Generative Models in Decision Making: A Survey | Generative models have fundamentally reshaped the landscape of decision-making, reframing the problem from pure scalar reward maximization to high-fidelity trajectory generation and distribution matching.
- [ ] relevant | `2503.10638v3` | Studying Classifier(-Free) Guidance From a Classifier-Centric Perspective | Classifier-free guidance has become a staple for conditional generation with denoising diffusion models.
- [ ] relevant | `2505.20199v1` | Adaptive Classifier-Free Guidance via Dynamic Low-Confidence Masking | Classifier-Free Guidance (CFG) significantly enhances controllability in generative models by interpolating conditional and unconditional predictions.
- [ ] relevant | `2506.14399v5` | Factored Classifier-Free Guidance | Counterfactual generation aims to simulate realistic hypothetical outcomes under causal interventions.
- [ ] relevant | `2507.08965v2` | Improving Classifier-Free Guidance in Masked Diffusion: Low-Dim Theoretical Insights with High-Dim Impact | Classifier-Free Guidance (CFG) is a widely used technique for conditional generation and improving sample quality in continuous diffusion models, and its extensions to discrete diffusion has recently started to be investigated.
- [ ] relevant | `2601.21868v2` | On Forgetting and Stability of Score-based Generative models | Understanding the stability and long-time behavior of generative models is a fundamental problem in modern machine learning.
- [ ] relevant | `2603.08155v3` | C$^2$FG: Control Classifier-Free Guidance via Score Discrepancy Analysis | Classifier-Free Guidance (CFG) is a cornerstone of modern conditional diffusion models, yet its reliance on the fixed or heuristic dynamic guidance weight is predominantly empirical and overlooks the inherent dynamics of the diffusion process.
- [ ] relevant | `2605.28036v1` | Stay Fair! Ensuring Group Fairness in Diffusion Models Across Guidance Scales | Diffusion models steer conditional generation with a tunable guidance scale to trade off prompt alignment and diversity.
- [x] relevant (gold) | `2606.13295v2` | Simultaneous Latent Budget Trees for Stratified Classification | In the era of Explainable Artificial Intelligence, there is a renewed focus on single trees for their ease of interpretation.

## Q34

**Question:** What happens to long-range stability when sequential dependence between latent variables is removed from a variational language model with a Gaussian-process prior?

**Gold:** `2512.24102v1` | Autoregressivity in the Latent Space of a GP-VAE Language Model: An Empirical Ablation Study

> This paper provides an ablation-based analysis of latent autoregression in GP-VAE models, building upon our previous work introducing the architecture. Language models typically rely on an autoregressive factorization over tokens.

**Candidates:**

- [ ] relevant | `2101.12072v2` | Autoregressive Denoising Diffusion Models for Multivariate Probabilistic Time Series Forecasting | In this work, we propose \texttt{TimeGrad}, an autoregressive model for multivariate probabilistic time series forecasting which samples from the data distribution at each time step by estimating its gradient.
- [ ] relevant | `2106.05931v3` | Score-based Generative Modeling in Latent Space | Score-based generative models (SGMs) have recently demonstrated impressive results in terms of both sample quality and distribution coverage.
- [ ] relevant | `2108.06084v4` | The Stability-Efficiency Dilemma: Investigating Sequence Length Warmup for Training GPT Models | Recent works have demonstrated great success in pre-training large-scale autoregressive language models on massive GPUs.
- [ ] relevant | `2302.08510v2` | Text-driven Visual Synthesis with Latent Diffusion Prior | There has been tremendous progress in large-scale text-to-image synthesis driven by diffusion models enabling versatile downstream applications such as 3D object synthesis from texts, image editing, and customized generation.
- [ ] relevant | `2303.02490v2` | Diffusion Models Generate Images Like Painters: an Analytical Theory of Outline First, Details Later | How do diffusion generative models convert pure noise into meaningful images?
- [ ] relevant | `2304.04746v1` | A Cheaper and Better Diffusion Language Model with Soft-Masked Noise | Diffusion models that are based on iterative denoising have been recently proposed and leveraged in various generation tasks like image generation.
- [ ] relevant | `2505.20199v1` | Adaptive Classifier-Free Guidance via Dynamic Low-Confidence Masking | Classifier-Free Guidance (CFG) significantly enhances controllability in generative models by interpolating conditional and unconditional predictions.
- [ ] relevant | `2507.04794v1` | Generalization bounds for score-based generative models: a synthetic proof | We establish minimax convergence rates for score-based generative models (SGMs) under the $1$-Wasserstein distance.
- [ ] relevant | `2509.22007v2` | Stage-wise Dynamics of Classifier-Free Guidance in Diffusion Models | Classifier-Free Guidance (CFG) is widely used to improve conditional fidelity in diffusion models, but its impact on sampling dynamics remains poorly understood.
- [x] relevant (gold) | `2512.24102v1` | Autoregressivity in the Latent Space of a GP-VAE Language Model: An Empirical Ablation Study | This paper provides an ablation-based analysis of latent autoregression in GP-VAE models, building upon our previous work introducing the architecture.
- [ ] relevant | `2601.21868v2` | On Forgetting and Stability of Score-based Generative models | Understanding the stability and long-time behavior of generative models is a fundamental problem in modern machine learning.
- [ ] relevant | `2602.07546v1` | Improving Variable-Length Generation in Diffusion Language Models via Length Regularization | Diffusion Large Language Models (DLLMs) are inherently ill-suited for variable-length generation, as their inference is defined on a fixed-length canvas and implicitly assumes a known target length.
- [ ] relevant | `2606.16360v1` | Tyler: Typed Latent Reasoning for Language Models -- When to Think, What to Compute, and How Much to Allocate | Chain-of-thought (CoT) prompting improves reasoning in large language models (LLMs) by externalizing intermediate computation as discrete text tokens, but this textual interface also introduces redundancy and inference overhead.

## Q35

**Question:** How can a language model decide, during decoding, when to reason in continuous hidden representations instead of writing out intermediate steps, and how much compute to spend on it?

**Gold:** `2606.16360v1` | Tyler: Typed Latent Reasoning for Language Models -- When to Think, What to Compute, and How Much to Allocate

> Chain-of-thought (CoT) prompting improves reasoning in large language models (LLMs) by externalizing intermediate computation as discrete text tokens, but this textual interface also introduces redundancy and inference overhead. Latent reasoning offers a promising alternative by carrying part of the computation in continuous representations.

**Candidates:**

- [ ] relevant | `2108.06084v4` | The Stability-Efficiency Dilemma: Investigating Sequence Length Warmup for Training GPT Models | Recent works have demonstrated great success in pre-training large-scale autoregressive language models on massive GPUs.
- [ ] relevant | `2212.00006v1` | Operationalizing Specifications, In Addition to Test Sets for Evaluating Constrained Generative Models | In this work, we present some recommendations on the evaluation of state-of-the-art generative models for constrained generation tasks.
- [ ] relevant | `2212.11685v2` | Text Generation with Diffusion Language Models: A Pre-training Approach with Continuous Paragraph Denoise | In this paper, we introduce a novel dIffusion language modEl pre-training framework for text generation, which we call GENIE.
- [ ] relevant | `2302.14368v5` | Enhanced Controllability of Diffusion Models via Feature Disentanglement and Realism-Enhanced Sampling Methods | As Diffusion Models have shown promising performance, a lot of efforts have been made to improve the controllability of Diffusion Models.
- [ ] relevant | `2304.04746v1` | A Cheaper and Better Diffusion Language Model with Soft-Masked Noise | Diffusion models that are based on iterative denoising have been recently proposed and leveraged in various generation tasks like image generation.
- [ ] relevant | `2310.05264v5` | The Emergence of Reproducibility and Generalizability in Diffusion Models | In this work, we investigate an intriguing and prevalent phenomenon of diffusion models which we term as "consistent model reproducibility": given the same starting noise input and a deterministic sampler, different diffusion models often yield remarkably similar outputs.
- [ ] relevant | `2411.17608v2` | Mixed-State Quantum Denoising Diffusion Probabilistic Model | Generative quantum machine learning has gained significant attention for its ability to produce quantum states with desired distributions.
- [ ] relevant | `2503.10638v3` | Studying Classifier(-Free) Guidance From a Classifier-Centric Perspective | Classifier-free guidance has become a staple for conditional generation with denoising diffusion models.
- [ ] relevant | `2505.04999v1` | CLAM: Continuous Latent Action Models for Robot Learning from Unlabeled Demonstrations | Learning robot policies using imitation learning requires collecting large amounts of costly action-labeled expert demonstrations, which fundamentally limits the scale of training data.
- [ ] relevant | `2505.20199v1` | Adaptive Classifier-Free Guidance via Dynamic Low-Confidence Masking | Classifier-Free Guidance (CFG) significantly enhances controllability in generative models by interpolating conditional and unconditional predictions.
- [ ] relevant | `2512.24102v1` | Autoregressivity in the Latent Space of a GP-VAE Language Model: An Empirical Ablation Study | This paper provides an ablation-based analysis of latent autoregression in GP-VAE models, building upon our previous work introducing the architecture.
- [ ] relevant | `2601.22468v1` | Training-Free Representation Guidance for Diffusion Models with a Representation Alignment Projector | Recent progress in generative modeling has enabled high-quality visual synthesis with diffusion-based frameworks, supporting controllable sampling and large-scale training.
- [ ] relevant | `2602.07546v1` | Improving Variable-Length Generation in Diffusion Language Models via Length Regularization | Diffusion Large Language Models (DLLMs) are inherently ill-suited for variable-length generation, as their inference is defined on a fixed-length canvas and implicitly assumes a known target length.
- [x] relevant (gold) | `2606.16360v1` | Tyler: Typed Latent Reasoning for Language Models -- When to Think, What to Compute, and How Much to Allocate | Chain-of-thought (CoT) prompting improves reasoning in large language models (LLMs) by externalizing intermediate computation as discrete text tokens, but this textual interface also introduces redundancy and inference overhead.

## Q36

**Question:** What success rate did an autonomous AI agent achieve at designing antibodies that were confirmed to bind in the lab, and how much faster were experts who used it?

**Gold:** `2603.29727v2` | Latent-Y: A Lab-Validated Autonomous Agent for De Novo Drug Design

> Drug discovery relies on iterative expert workflows that are slow to parallelize and difficult to scale. Here we introduce Latent-Y, an AI agent that autonomously executes complete antibody design campaigns from text prompts, covering literature review, target analysis, epitope identification, candidate design, computational validation, and selection of lab-ready sequences.

**Candidates:**

- [ ] relevant | `0405062v1` | Efficiency Enhancement of Probabilistic Model Building Genetic Algorithms | This paper presents two different efficiency-enhancement techniques for probabilistic model building genetic algorithms.
- [ ] relevant | `2101.04525v2` | A comparison of optimisation algorithms for high-dimensional particle and astrophysics applications | Optimisation problems are ubiquitous in particle and astrophysics, and involve locating the optimum of a complicated function of many parameters that may be computationally expensive to evaluate.
- [ ] relevant | `2301.06871v1` | Denoising Diffusion Probabilistic Models as a Defense against Adversarial Attacks | Neural Networks are infamously sensitive to small perturbations in their inputs, making them vulnerable to adversarial attacks.
- [ ] relevant | `2307.03421v1` | Non-iterative Coarse-to-fine Transformer Networks for Joint Affine and Deformable Image Registration | Image registration is a fundamental requirement for medical image analysis.
- [ ] relevant | `2312.01242v1` | DDxT: Deep Generative Transformer Models for Differential Diagnosis | Differential Diagnosis (DDx) is the process of identifying the most likely medical condition among the possible pathologies through the process of elimination based on evidence.
- [ ] relevant | `2402.13144v3` | Neural Network Diffusion | Diffusion models have achieved remarkable success in image and video generation.
- [ ] relevant | `2409.00588v3` | Diffusion Policy Policy Optimization | We introduce Diffusion Policy Policy Optimization, DPPO, an algorithmic framework including best practices for fine-tuning diffusion-based policies (e.g.
- [ ] relevant | `2502.17100v4` | Generative Models in Decision Making: A Survey | Generative models have fundamentally reshaped the landscape of decision-making, reframing the problem from pure scalar reward maximization to high-fidelity trajectory generation and distribution matching.
- [ ] relevant | `2505.04999v1` | CLAM: Continuous Latent Action Models for Robot Learning from Unlabeled Demonstrations | Learning robot policies using imitation learning requires collecting large amounts of costly action-labeled expert demonstrations, which fundamentally limits the scale of training data.
- [ ] relevant | `2507.05482v3` | Stein Diffusion Guidance: Training-Free Posterior Correction for Sampling Beyond High-Density Regions | Training-free diffusion guidance offers a flexible framework for leveraging off-the-shelf classifiers without additional training.
- [ ] relevant | `2507.19375v1` | Latent-X: An Atom-level Frontier Model for De Novo Protein Binder Design | Traditional drug discovery relies on rounds of screening millions of candidate molecules with low success rates, making drug discovery time and resource intensive.
- [ ] relevant | `2510.09786v1` | Enhancing Diffusion Policy with Classifier-Free Guidance for Temporal Robotic Tasks | Temporal sequential tasks challenge humanoid robots, as existing Diffusion Policy (DP) and Action Chunking with Transformers (ACT) methods often lack temporal context, resulting in local optima traps and excessive repetitive actions.
- [ ] relevant | `2510.16223v1` | Case Study of GAI for Generating Novel Images for Real-World Embroidery | In this paper, we present a case study exploring the potential use of Generative Artificial Intelligence (GAI) to address the real-world need of making the design of embroiderable art patterns more accessible.
- [ ] relevant | `2512.20263v1` | Drug-like antibodies with low immunogenicity in human panels designed with Latent-X2 | Drug discovery has long sought computational systems capable of designing drug-like molecules directly: developable and non-immunogenic from the start.
- [x] relevant (gold) | `2603.29727v2` | Latent-Y: A Lab-Validated Autonomous Agent for De Novo Drug Design | Drug discovery relies on iterative expert workflows that are slow to parallelize and difficult to scale.

## Q37

**Question:** Which generative model jointly produces the full atomic structure and sequence of a binder for a given protein epitope, and what experimental hit rates did it reach?

**Gold:** `2507.19375v1` | Latent-X: An Atom-level Frontier Model for De Novo Protein Binder Design

> Traditional drug discovery relies on rounds of screening millions of candidate molecules with low success rates, making drug discovery time and resource intensive. To overcome this screening bottleneck, we introduce Latent-X, an all-atom protein design model that enables a new paradigm of precision AI design.

**Candidates:**

- [ ] relevant | `2112.07068v4` | Score-Based Generative Modeling with Critically-Damped Langevin Diffusion | Score-based generative models (SGMs) have demonstrated remarkable synthesis quality.
- [ ] relevant | `2202.02763v3` | Riemannian Score-Based Generative Modelling | Score-based generative models (SGMs) are a powerful class of generative models that exhibit remarkable empirical performance.
- [ ] relevant | `2203.04698v1` | Score-Based Generative Models for Molecule Generation | Recent advances in generative models have made exploring design spaces easier for de novo molecule generation.
- [ ] relevant | `2206.11898v3` | Score-based Generative Models for Calorimeter Shower Simulation | Score-based generative models are a new class of generative algorithms that have been shown to produce realistic images even in high dimensional spaces, currently surpassing other state-of-the-art models for different benchmark categories and applications.
- [ ] relevant | `2211.01364v3` | An optimal control perspective on diffusion-based generative modeling | We establish a connection between stochastic optimal control and generative models based on stochastic differential equations (SDEs), such as recently developed diffusion probabilistic models.
- [ ] relevant | `2212.06359v1` | Score-based Generative Modeling Secretly Minimizes the Wasserstein Distance | Score-based generative models are shown to achieve remarkable empirical performances in various applications such as image generation and audio synthesis.
- [ ] relevant | `2312.10527v2` | CoCoGen: Physically-Consistent and Conditioned Score-based Generative Models for Forward and Inverse Problems | Recent advances in generative artificial intelligence have had a significant impact on diverse domains spanning computer vision, natural language processing, and drug discovery.
- [ ] relevant | `2402.06079v2` | DiscDiff: Latent Diffusion Model for DNA Sequence Generation | This paper introduces a novel framework for DNA sequence generation, comprising two key components: DiscDiff, a Latent Diffusion Model (LDM) tailored for generating discrete DNA sequences, and Absorb-Escape, a post-training algorithm designed to refine these sequences.
- [ ] relevant | `2507.04794v1` | Generalization bounds for score-based generative models: a synthetic proof | We establish minimax convergence rates for score-based generative models (SGMs) under the $1$-Wasserstein distance.
- [x] relevant (gold) | `2507.19375v1` | Latent-X: An Atom-level Frontier Model for De Novo Protein Binder Design | Traditional drug discovery relies on rounds of screening millions of candidate molecules with low success rates, making drug discovery time and resource intensive.
- [ ] relevant | `2510.22899v1` | On the Anisotropy of Score-Based Generative Models | We investigate the role of network architecture in shaping the inductive biases of modern score-based generative models.
- [ ] relevant | `2512.20263v1` | Drug-like antibodies with low immunogenicity in human panels designed with Latent-X2 | Drug discovery has long sought computational systems capable of designing drug-like molecules directly: developable and non-immunogenic from the start.
- [ ] relevant | `2603.29727v2` | Latent-Y: A Lab-Validated Autonomous Agent for De Novo Drug Design | Drug discovery relies on iterative expert workflows that are slow to parallelize and difficult to scale.

## Q38

**Question:** How can evolutionary optimisers that learn a probabilistic model of good solutions cut down on expensive fitness evaluations?

**Gold:** `0405062v1` | Efficiency Enhancement of Probabilistic Model Building Genetic Algorithms

> This paper presents two different efficiency-enhancement techniques for probabilistic model building genetic algorithms. The first technique proposes the use of a mutation operator which performs local search in the sub-solution neighborhood identified through the probabilistic model.

**Candidates:**

- [x] relevant (gold) | `0405062v1` | Efficiency Enhancement of Probabilistic Model Building Genetic Algorithms | This paper presents two different efficiency-enhancement techniques for probabilistic model building genetic algorithms.
- [ ] relevant | `2101.04525v2` | A comparison of optimisation algorithms for high-dimensional particle and astrophysics applications | Optimisation problems are ubiquitous in particle and astrophysics, and involve locating the optimum of a complicated function of many parameters that may be computationally expensive to evaluate.
- [ ] relevant | `2306.06684v1` | Happy People -- Image Synthesis as Black-Box Optimization Problem in the Discrete Latent Space of Deep Generative Models | In recent years, optimization in the learned latent space of deep generative models has been successfully applied to black-box optimization problems such as drug design, image generation or neural architecture search.
- [ ] relevant | `2306.15512v1` | Trajectory Generation, Control, and Safety with Denoising Diffusion Probabilistic Models | We present a framework for safety-critical optimal control of physical systems based on denoising diffusion probabilistic models (DDPMs).
- [ ] relevant | `2310.05264v5` | The Emergence of Reproducibility and Generalizability in Diffusion Models | In this work, we investigate an intriguing and prevalent phenomenon of diffusion models which we term as "consistent model reproducibility": given the same starting noise input and a deterministic sampler, different diffusion models often yield remarkably similar outputs.
- [ ] relevant | `2312.03397v1` | Generalized Contrastive Divergence: Joint Training of Energy-Based Model and Diffusion Model through Inverse Reinforcement Learning | We present Generalized Contrastive Divergence (GCD), a novel objective function for training an energy-based model (EBM) and a sampler simultaneously.
- [ ] relevant | `2407.00626v2` | Maximum Entropy Inverse Reinforcement Learning of Diffusion Models with Energy-Based Models | We present a maximum entropy inverse reinforcement learning (IRL) approach for improving the sample quality of diffusion generative models, especially when the number of generation time steps is small.
- [ ] relevant | `2409.00588v3` | Diffusion Policy Policy Optimization | We introduce Diffusion Policy Policy Optimization, DPPO, an algorithmic framework including best practices for fine-tuning diffusion-based policies (e.g.
- [ ] relevant | `2502.08808v2` | A First-order Generative Bilevel Optimization Framework for Diffusion Models | Diffusion models, which iteratively denoise data samples to synthesize high-quality outputs, have achieved empirical success across domains.
- [ ] relevant | `2502.12146v1` | Diffusion-Sharpening: Fine-tuning Diffusion Models with Denoising Trajectory Sharpening | We propose Diffusion-Sharpening, a fine-tuning approach that enhances downstream alignment by optimizing sampling trajectories.
- [ ] relevant | `2502.17100v4` | Generative Models in Decision Making: A Survey | Generative models have fundamentally reshaped the landscape of decision-making, reframing the problem from pure scalar reward maximization to high-fidelity trajectory generation and distribution matching.
- [ ] relevant | `2507.05482v3` | Stein Diffusion Guidance: Training-Free Posterior Correction for Sampling Beyond High-Density Regions | Training-free diffusion guidance offers a flexible framework for leveraging off-the-shelf classifiers without additional training.
- [ ] relevant | `2509.16131v2` | Dynamic Classifier-Free Diffusion Guidance via Online Feedback | Classifier-free guidance (CFG) is a cornerstone of text-to-image diffusion models, yet its effectiveness is limited by the use of static guidance scales.
- [ ] relevant | `2603.08155v3` | C$^2$FG: Control Classifier-Free Guidance via Score Discrepancy Analysis | Classifier-Free Guidance (CFG) is a cornerstone of modern conditional diffusion models, yet its reliance on the fixed or heuristic dynamic guidance weight is predominantly empirical and overlooks the inherent dynamics of the diffusion process.

## Q39

**Question:** How can safety constraints be enforced when control trajectories for a physical system are planned by iterative denoising?

**Gold:** `2306.15512v1` | Trajectory Generation, Control, and Safety with Denoising Diffusion Probabilistic Models

> We present a framework for safety-critical optimal control of physical systems based on denoising diffusion probabilistic models (DDPMs). The technology of control barrier functions (CBFs), encoding desired safety constraints, is used in combination with DDPMs to plan actions by iteratively denoising trajectories through a CBF-based guided sampling procedure.

**Candidates:**

- [ ] relevant | `2211.01364v3` | An optimal control perspective on diffusion-based generative modeling | We establish a connection between stochastic optimal control and generative models based on stochastic differential equations (SDEs), such as recently developed diffusion probabilistic models.
- [ ] relevant | `2301.06871v1` | Denoising Diffusion Probabilistic Models as a Defense against Adversarial Attacks | Neural Networks are infamously sensitive to small perturbations in their inputs, making them vulnerable to adversarial attacks.
- [x] relevant (gold) | `2306.15512v1` | Trajectory Generation, Control, and Safety with Denoising Diffusion Probabilistic Models | We present a framework for safety-critical optimal control of physical systems based on denoising diffusion probabilistic models (DDPMs).
- [ ] relevant | `2310.12609v4` | Denoising Heat-inspired Diffusion with Insulators for Collision Free Motion Planning | Diffusion models have risen as a powerful tool in robotics due to their flexibility and multi-modality.
- [ ] relevant | `2311.10868v1` | SDDPM: Speckle Denoising Diffusion Probabilistic Models | Coherent imaging systems, such as medical ultrasound and synthetic aperture radar (SAR), are subject to corruption from speckle due to sub-resolution scatterers.
- [ ] relevant | `2312.05320v4` | Uncertainty-aware Surrogate Models for Airfoil Flow Simulations with Denoising Diffusion Probabilistic Models | Leveraging neural networks as surrogate models for turbulence simulation is a topic of growing interest.
- [ ] relevant | `2312.07586v5` | Characteristic Guidance: Non-linear Correction for Diffusion Model at Large Guidance Scale | Popular guidance for denoising diffusion probabilistic model (DDPM) linearly combines distinct conditional models together to provide enhanced control over samples.
- [ ] relevant | `2401.05779v4` | Erasing Undesirable Influence in Diffusion Models | Diffusion models are highly effective at generating high-quality images but pose risks, such as the unintentional generation of NSFW (not safe for work) content.
- [ ] relevant | `2410.09945v2` | Variational Diffusion Posterior Sampling with Midpoint Guidance | Diffusion models have recently shown considerable potential in solving Bayesian inverse problems when used as priors.
- [ ] relevant | `2502.17100v4` | Generative Models in Decision Making: A Survey | Generative models have fundamentally reshaped the landscape of decision-making, reframing the problem from pure scalar reward maximization to high-fidelity trajectory generation and distribution matching.
- [ ] relevant | `2507.18654v2` | Diffusion Models for Solving Inverse Problems via Posterior Sampling with Piecewise Guidance | Diffusion models are powerful tools for sampling from high-dimensional distributions by progressively transforming pure noise into structured data through a denoising process.
- [ ] relevant | `2511.09180v1` | FSampler: Training Free Acceleration of Diffusion Sampling via Epsilon Extrapolation | FSampler is a training free, sampler agnostic execution layer that accelerates diffusion sampling by reducing the number of function evaluations (NFE).
- [ ] relevant | `2603.08155v3` | C$^2$FG: Control Classifier-Free Guidance via Score Discrepancy Analysis | Classifier-Free Guidance (CFG) is a cornerstone of modern conditional diffusion models, yet its reliance on the fixed or heuristic dynamic guidance weight is predominantly empirical and overlooks the inherent dynamics of the diffusion process.
- [ ] relevant | `2605.06831v2` | Why DDIM Hallucinates More Than DDPM: A Theoretical Analysis of Reverse Dynamics | We theoretically study the hallucination phenomena in two canonical diffusion samplers: the stochastic Denoising Diffusion Probabilistic Model (DDPM) and the deterministic Denoising Diffusion Implicit Model (DDIM).
- [ ] relevant | `2605.27990v1` | Geometry-Correct Diffusion Posterior Sampling with Denoiser-Pullback Curvature Guidance and Manifold-Aligned Damping | Diffusion posterior sampling conditions diffusion priors on measurements, but data-consistency updates are typically scaled by hand-tuned guidance weights and can destabilize sampling under stiff, operator-dependent curvature.

## Q40

**Question:** How can quantities such as mutual information and estimation-error bounds be estimated from data for wireless systems that share spectrum between sensing and data transmission?

**Gold:** `2508.02117v1` | Scoring ISAC: Benchmarking Integrated Sensing and Communications via Score-Based Generative Modeling

> Integrated sensing and communications (ISAC) is a key enabler for next-generation wireless systems, aiming to support both high-throughput communication and high-accuracy environmental sensing using shared spectrum and hardware. Theoretical performance metrics, such as mutual information (MI), minimum mean squared error (MMSE), and Bayesian Cramér--Rao bound (BCRB), play a key role in evaluating ISAC system performance limits.

**Candidates:**

- [ ] relevant | `2211.01364v3` | An optimal control perspective on diffusion-based generative modeling | We establish a connection between stochastic optimal control and generative models based on stochastic differential equations (SDEs), such as recently developed diffusion probabilistic models.
- [ ] relevant | `2212.06359v1` | Score-based Generative Modeling Secretly Minimizes the Wasserstein Distance | Score-based generative models are shown to achieve remarkable empirical performances in various applications such as image generation and audio synthesis.
- [ ] relevant | `2309.08568v2` | Denoising Diffusion Probabilistic Models for Hardware-Impaired Communications | Generative AI has received significant attention among a spectrum of diverse industrial and academic domains, thanks to the magnificent results achieved from deep generative models such as generative pre-trained transformers (GPT) and diffusion models.
- [ ] relevant | `2309.08688v1` | Probabilistic Constellation Shaping With Denoising Diffusion Probabilistic Models: A Novel Approach | With the incredible results achieved from generative pre-trained transformers (GPT) and diffusion models, generative AI (GenAI) is envisioned to yield remarkable breakthroughs in various industrial and academic domains.
- [ ] relevant | `2311.10868v1` | SDDPM: Speckle Denoising Diffusion Probabilistic Models | Coherent imaging systems, such as medical ultrasound and synthetic aperture radar (SAR), are subject to corruption from speckle due to sub-resolution scatterers.
- [ ] relevant | `2402.02316v4` | Your Diffusion Model is Secretly a Certifiably Robust Classifier | Generative learning, recognized for its effective modeling of data distributions, offers inherent advantages in handling out-of-distribution instances, especially for enhancing robustness to adversarial attacks.
- [ ] relevant | `2402.03701v2` | Unified Discrete Diffusion for Categorical Data | Discrete diffusion models have seen a surge of attention with applications on naturally discrete data such as language and graphs.
- [ ] relevant | `2503.10638v3` | Studying Classifier(-Free) Guidance From a Classifier-Centric Perspective | Classifier-free guidance has become a staple for conditional generation with denoising diffusion models.
- [ ] relevant | `2506.21452v1` | Rethinking Oversaturation in Classifier-Free Guidance via Low Frequency | Classifier-free guidance (CFG) succeeds in condition diffusion models that use a guidance scale to balance the influence of conditional and unconditional terms.
- [ ] relevant | `2507.05454v2` | Risk-Aware Aerocapture Guidance Through a Probabilistic Indicator Function | Aerocapture is sensitive to trajectory errors, particularly for low-cost missions with imprecise navigation.
- [ ] relevant | `2507.18654v2` | Diffusion Models for Solving Inverse Problems via Posterior Sampling with Piecewise Guidance | Diffusion models are powerful tools for sampling from high-dimensional distributions by progressively transforming pure noise into structured data through a denoising process.
- [x] relevant (gold) | `2508.02117v1` | Scoring ISAC: Benchmarking Integrated Sensing and Communications via Score-Based Generative Modeling | Integrated sensing and communications (ISAC) is a key enabler for next-generation wireless systems, aiming to support both high-throughput communication and high-accuracy environmental sensing using shared spectrum and hardware.
- [ ] relevant | `2603.25384v1` | Underdetermined Blind Source Separation via Weighted Simplex Shrinkage Regularization and Quantum Deep Image Prior | As most optical satellites remotely acquire multispectral images (MSIs) with limited spatial resolution, multispectral unmixing (MU) becomes a critical signal processing technology for analyzing the pure material spectra for high-precision classification and identification.
- [ ] relevant | `2605.30330v1` | When, why, and how do diffusion posterior samplers fail? A finite-sample lens | Diffusion models have excellent capacity to model complex distributions of natural data, which has made them a popular and effective choice for posterior sampling in imaging inverse problems.

# Out-of-domain questions

Expected behaviour: the system abstains. Delete a line to drop that question, or edit the text.
For near-miss questions the keyword counts and the three nearest abstracts are shown so you can confirm the corpus really lacks the answer.

## Off-topic

- `O01` | What is the boiling point of water at the summit of Mount Everest?
- `O02` | Which country won the FIFA World Cup in 2010?
- `O03` | How should I prune a tomato plant to get more fruit?
- `O04` | What causes the seasons on Earth?
- `O05` | What is the difference between a Roth IRA and a traditional IRA?
- `O06` | How does TCP congestion control decide when to slow down?

## Near-miss

- `O07` | How do consistency models enable single-step image generation?
  - keyword hits in papers.json: "consistency model": 0
  - nearest: `2501.13926v2` | Can We Generate Images with CoT? Let's Verify and Reinforce Image Generation Step by Step | Chain-of-Thought (CoT) reasoning has been extensively explored in large models to tackle complex understanding tasks.
  - nearest: `2303.02490v2` | Diffusion Models Generate Images Like Painters: an Analytical Theory of Outline First, Details Later | How do diffusion generative models convert pure noise into meaningful images?
  - nearest: `2409.19365v3` | Conditional Image Synthesis with Diffusion Models: A Survey | Conditional image synthesis based on user-specified requirements is a key component in creating complex visual content.
- `O08` | How does Fick's second law describe the diffusion of a solute through a liquid?
  - keyword hits in papers.json: "Fick": 0, "heat equation": 0, "Brownian": 0
  - nearest: `1905.04004v2` | Well-posedness of a cross-diffusion population model with nonlocal diffusion | We prove the existence and uniqueness of solution of a nonlocal cross-diffusion competitive population model for two species.
  - nearest: `2006.11239v2` | Denoising Diffusion Probabilistic Models | We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics.
  - nearest: `2605.22586v3` | A Tutorial on Diffusion Theory: From Differential Equations to Diffusion Models | Diffusion models have emerged as a dominant framework for generative modeling, but their mathematical foundations are often presented separately through diffusion probabilistic models, score-based modeling, stochastic differential equations, and numerical sampling methods.
- `O09` | How does the gradient penalty stabilise the training of a Wasserstein GAN?
  - keyword hits in papers.json: "gradient penalty": 0, "Wasserstein GAN": 0, "WGAN": 0
  - nearest: `2206.02262v4` | Diffusion-GAN: Training GANs with Diffusion | Generative adversarial networks (GANs) are challenging to train stably, and a promising remedy of injecting instance noise into the discriminator input has not been very effective in practice.
  - nearest: `2507.04794v1` | Generalization bounds for score-based generative models: a synthetic proof | We establish minimax convergence rates for score-based generative models (SGMs) under the $1$-Wasserstein distance.
  - nearest: `2111.02316v1` | Improving Model Compatibility of Generative Adversarial Networks by Boundary Calibration | Generative Adversarial Networks (GANs) is a powerful family of models that learn an underlying distribution to generate synthetic data.
- `O10` | How does bias correction work in the Adam optimizer?
  - keyword hits in papers.json: "bias correction": 0, "Adam": 0
  - nearest: `2510.22899v1` | On the Anisotropy of Score-Based Generative Models | We investigate the role of network architecture in shaping the inductive biases of modern score-based generative models.
  - nearest: `2507.05482v3` | Stein Diffusion Guidance: Training-Free Posterior Correction for Sampling Beyond High-Density Regions | Training-free diffusion guidance offers a flexible framework for leveraging off-the-shelf classifiers without additional training.
  - nearest: `2502.12146v1` | Diffusion-Sharpening: Fine-tuning Diffusion Models with Denoising Trajectory Sharpening | We propose Diffusion-Sharpening, a fine-tuning approach that enhances downstream alignment by optimizing sampling trajectories.
- `O11` | What does the Evoformer module do in AlphaFold?
  - keyword hits in papers.json: "Evoformer": 0, "AlphaFold": 0
  - nearest: `2511.09180v1` | FSampler: Training Free Acceleration of Diffusion Sampling via Epsilon Extrapolation | FSampler is a training free, sampler agnostic execution layer that accelerates diffusion sampling by reducing the number of function evaluations (NFE).
  - nearest: `2507.19375v1` | Latent-X: An Atom-level Frontier Model for De Novo Protein Binder Design | Traditional drug discovery relies on rounds of screening millions of candidate molecules with low success rates, making drug discovery time and resource intensive.
  - nearest: `2603.29727v2` | Latent-Y: A Lab-Validated Autonomous Agent for De Novo Drug Design | Drug discovery relies on iterative expert workflows that are slow to parallelize and difficult to scale.
- `O12` | How can a membership inference attack reveal whether an image was in a diffusion model's training set?
  - keyword hits in papers.json: "membership inference": 0
  - nearest: `2303.09295v1` | DIRE for Diffusion-Generated Image Detection | Diffusion models have shown remarkable success in visual synthesis, but have also raised concerns about potential abuse for malicious purposes.
  - nearest: `2404.07724v2` | Applying Guidance in a Limited Interval Improves Sample and Distribution Quality in Diffusion Models | Guidance is a crucial technique for extracting the best performance out of image-generating diffusion models.
  - nearest: `2207.12598v1` | Classifier-Free Diffusion Guidance | Classifier guidance is a recently introduced method to trade off mode coverage and sample fidelity in conditional diffusion models post training, in the same spirit as low temperature sampling or truncation in other types of generative models.
