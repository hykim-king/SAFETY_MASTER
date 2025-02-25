package com.pcwk.ehr.earthquake.domain;

public class EarthquakeVO {

    // 필드 정의 (테이블의 컬럼에 해당)
    private int eqkNum;
    private int eqkAreaRegion;
    private String eqkReportTime;
    private String eqkOriginTime;
    private double eqkMt;
    private double eqkLat;
    private double eqkLon;
    private String eqkLoc;
    private int eqkIntensity;
    private String eqkComments;   
    private String eqkUpdate;
    private String eqkOriginMsc;

    // Getter와 Setter 메서드들

    public int getEqkNum() {
        return eqkNum;
    }

    public void setEqkNum(int eqkNum) {
        this.eqkNum = eqkNum;
    }

    public int getEqkAreaRegion() {
        return eqkAreaRegion;
    }

    public void setEqkAreaRegion(int eqkAreaRegion) {
        this.eqkAreaRegion = eqkAreaRegion;
    }

    public String getEqkReportTime() {
        return eqkReportTime;
    }

    public void setEqkReportTime(String eqkReportTime) {
        this.eqkReportTime = eqkReportTime;
    }

    public String getEqkOriginTime() {
        return eqkOriginTime;
    }

    public void setEqkOriginTime(String eqkOriginTime) {
        this.eqkOriginTime = eqkOriginTime;
    }

    public double getEqkMt() {
        return eqkMt;
    }

    public void setEqkMt(double eqkMt) {
        this.eqkMt = eqkMt;
    }

    public double getEqkLat() {
        return eqkLat;
    }

    public void setEqkLat(double eqkLat) {
        this.eqkLat = eqkLat;
    }

    public double getEqkLon() {
        return eqkLon;
    }

    public void setEqkLon(double eqkLon) {
        this.eqkLon = eqkLon;
    }

    public String getEqkLoc() {
        return eqkLoc;
    }

    public void setEqkLoc(String eqkLoc) {
        this.eqkLoc = eqkLoc;
    }

    public int getEqkIntensity() {
        return eqkIntensity;
    }

    public void setEqkIntensity(int eqkIntensity) {
        this.eqkIntensity = eqkIntensity;
    }

    public String getEqkComments() {
        return eqkComments;
    }

    public void setEqkComments(String eqkComments) {
        this.eqkComments = eqkComments;
    }

    public String getEqkUpdate() {
        return eqkUpdate;
    }

    public void setEqkUpdate(String eqkUpdate) {
        this.eqkUpdate = eqkUpdate;
    }

    public String getEqkOriginMsc() {
        return eqkOriginMsc;
    }

    public void setEqkOriginMsc(String eqkOriginMsc) {
        this.eqkOriginMsc = eqkOriginMsc;
    }

    // toString 메서드 (객체를 문자열로 출력하기 위한 용도)
    @Override
    public String toString() {
        return "EarthquakeVO{" +
                "eqkNum=" + eqkNum +
                ", eqkAreaRegion=" + eqkAreaRegion +
                ", eqkReportTime='" + eqkReportTime + '\'' +
                ", eqkOriginTime='" + eqkOriginTime + '\'' +
                ", eqkMt=" + eqkMt +
                ", eqkLat=" + eqkLat +
                ", eqkLon=" + eqkLon +
                ", eqkLoc='" + eqkLoc + '\'' +
                ", eqkIntensity=" + eqkIntensity +
                ", eqkComments='" + eqkComments + '\'' +
                ", eqkUpdate='" + eqkUpdate + '\'' +
                ", eqkOriginMsc='" + eqkOriginMsc + '\'' +
                '}';
    }
}
