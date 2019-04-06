# Medical Image Segmentation 
Segmentation of Lungs from Chest X-rays. 

- Lung segmentation with UNet architecture (e.g Keras layers in UNet, modelling, training, testing)
- Data loading, data generators, and image augmentation
- Training/Validation through generator 
- Callbacks (e.g. DICE score)
- Visualization

# Output
Format : Predicted&emsp;GoldStd&emsp;Diff <br>
![alt img](./output.gif) <br>

# Further Tasks: 
- To explore other segmentations networks like LinkNet, Mask R-CNN
- Build an ensemble model on top of these models 

------------------ 
### About the data
Disclaimer: Please do not share the data set outside of your research group/organization, but forward new data set requests to Sameer Antani, project leader at National Library of Medicine of the National Institutes of Health. *

IRB Details: The dataset were de-identified by the data providers and were exempted from IRB review at their institutions. The data set use and public release were exempted from IRB review (No. 5357) by the NIH Office of Human Research Projections Programs.

References
1)  Candemir S, Jaeger S, Musco J, Xue Z, Karargyris A, Antani SK, Thoma GR, Palaniappan K. Lung segmentation in chest radiographs using anatomical atlases with nonrigid registration. IEEE Trans Med Imaging. 2014 Feb;33(2):577-90. doi: 10.1109/TMI.2013.2290491. PMID: 24239990 
2)  Jaeger S, Karargyris A, Candemir S, Folio L, Siegelman J, Callaghan FM, Xue Z, Palaniappan K, Singh RK, Antani SK. Automatic tuberculosis screening using chest radiographs. IEEE Trans Med Imaging. 2014 Feb;33(2):233-45. doi: 10.1109/TMI.2013.2284099. PMID: 24108713 

*https://ceb.nlm.nih.gov/repositories/tuberculosis-chest-x-ray-image-data-sets/
