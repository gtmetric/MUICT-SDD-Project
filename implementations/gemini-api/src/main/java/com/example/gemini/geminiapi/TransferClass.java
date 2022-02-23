package com.example.gemini.geminiapi;

import edu.gemini.app.ocs.OCS;
import edu.gemini.app.ocs.model.DataProcRequirement;
import edu.gemini.app.ocs.model.SciencePlan;
import edu.gemini.app.ocs.model.StarSystem;


public class TransferClass {
    int planNo;
    String creator;
    String submitter;
    double fundingInUSD;
    String objectives;
    String starSystem;
    String startDate;
    String endDate;
    String telescopeLocation;
    String fileType;
    String fileQuality;
    String colorType;
    double contrast;
    double brightness;
    double saturation;
    double highlights;
    double exposure;
    double shadows;
    double whites;
    double blacks;
    double luminance;
    double hue;

    public SciencePlan toSciencePlan() {
        SciencePlan sp = new SciencePlan();
        sp.setCreator(creator);
        sp.setSubmitter(submitter);
        sp.setFundingInUSD(fundingInUSD);
        sp.setObjectives(objectives);
        sp.setStarSystem(StarSystem.CONSTELLATIONS.valueOf(starSystem));
        sp.setStartDate(startDate);
        sp.setTelescopeLocation(SciencePlan.TELESCOPELOC.valueOf(telescopeLocation));
        sp.setEndDate(endDate);
        DataProcRequirement dpr1 =
                new DataProcRequirement(fileType, fileQuality, colorType,
                        contrast, brightness, saturation, highlights, exposure, shadows,
                        whites, blacks, luminance, hue);
        sp.setDataProcRequirements(dpr1);

        return sp;
    }

    public SciencePlan updateSciencePlan() {
        OCS ocs = new OCS();
        SciencePlan sp = ocs.getSciencePlanByNo(planNo);
        sp.setCreator(creator);
        sp.setSubmitter(submitter);
        sp.setFundingInUSD(fundingInUSD);
        sp.setObjectives(objectives);
        sp.setStarSystem(StarSystem.CONSTELLATIONS.valueOf(starSystem));
        sp.setStartDate(startDate);
        sp.setTelescopeLocation(SciencePlan.TELESCOPELOC.valueOf(telescopeLocation));
        sp.setEndDate(endDate);
        DataProcRequirement dpr1 =
                new DataProcRequirement(fileType, fileQuality, colorType,
                        contrast, brightness, saturation, highlights, exposure, shadows,
                        whites, blacks, luminance, hue);
        sp.setDataProcRequirements(dpr1);

        return sp;
    }

    public int getPlanNo() {
        return planNo;
    }

    public void setPlanNo(int planNo) {
        this.planNo = planNo;
    }

    public String getCreator() {
        return creator;
    }

    public void setCreator(String creator) {
        this.creator = creator;
    }

    public String getSubmitter() {
        return submitter;
    }

    public void setSubmitter(String submitter) {
        this.submitter = submitter;
    }

    public double getFundingInUSD() {
        return fundingInUSD;
    }

    public void setFundingInUSD(double fundingInUSD) {
        this.fundingInUSD = fundingInUSD;
    }

    public String getObjectives() {
        return objectives;
    }

    public void setObjectives(String objectives) {
        this.objectives = objectives;
    }

    public String getStarSystem() {
        return starSystem;
    }

    public void setStarSystem(String starSystem) {
        this.starSystem = starSystem;
    }

    public String getStartDate() {
        return startDate;
    }

    public void setStartDate(String startDate) {
        this.startDate = startDate;
    }

    public String getEndDate() {
        return endDate;
    }

    public void setEndDate(String endDate) {
        this.endDate = endDate;
    }

    public String getTelescopeLocation() {
        return telescopeLocation;
    }

    public void setTelescopeLocation(String telescopeLocation) {
        this.telescopeLocation = telescopeLocation;
    }

    public String getFileType() {
        return fileType;
    }

    public void setFileType(String fileType) {
        this.fileType = fileType;
    }

    public String getFileQuality() {
        return fileQuality;
    }

    public void setFileQuality(String fileQuality) {
        this.fileQuality = fileQuality;
    }

    public String getColorType() {
        return colorType;
    }

    public void setColorType(String colorType) {
        this.colorType = colorType;
    }

    public double getContrast() {
        return contrast;
    }

    public void setContrast(double contrast) {
        this.contrast = contrast;
    }

    public double getBrightness() {
        return brightness;
    }

    public void setBrightness(double brightness) {
        this.brightness = brightness;
    }

    public double getSaturation() {
        return saturation;
    }

    public void setSaturation(double saturation) {
        this.saturation = saturation;
    }

    public double getHighlights() {
        return highlights;
    }

    public void setHighlights(double highlights) {
        this.highlights = highlights;
    }

    public double getExposure() {
        return exposure;
    }

    public void setExposure(double exposure) {
        this.exposure = exposure;
    }

    public double getShadows() {
        return shadows;
    }

    public void setShadows(double shadows) {
        this.shadows = shadows;
    }

    public double getWhites() {
        return whites;
    }

    public void setWhites(double whites) {
        this.whites = whites;
    }

    public double getBlacks() {
        return blacks;
    }

    public void setBlacks(double blacks) {
        this.blacks = blacks;
    }

    public double getLuminance() {
        return luminance;
    }

    public void setLuminance(double luminance) {
        this.luminance = luminance;
    }

    public double getHue() {
        return hue;
    }

    public void setHue(double hue) {
        this.hue = hue;
    }
}
