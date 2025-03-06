package com.pcwk.ehr.air_quality.domain;

import java.util.Objects;

public class Air_QualityVO {

	private long aq_Id;
	private String gu_Cd;
	private String gu_Nm;
	private String ms_Addr;
	private double ms_Lat;
	private double ms_Lon;
	private int sort_Ord;
	private String cai_Grade;
	private int cai;
	private int pm25_Conc;
	private int pm10_Conc;
	private double o3_Conc;
	private String ms_Dt;
	private int crt_By;
	private String crt_Dt;
	private int mod_By;
	private String mod_Dt;

	public Air_QualityVO() {
		super();
	}

	public long getAq_Id() {
		return aq_Id;
	}

	public void setAq_Id(long aq_Id) {
		this.aq_Id = aq_Id;
	}

	public String getGu_Cd() {
		return gu_Cd;
	}

	public void setGu_Cd(String gu_Cd) {
		this.gu_Cd = gu_Cd;
	}

	public String getGu_Nm() {
		return gu_Nm;
	}

	public void setGu_Nm(String gu_Nm) {
		this.gu_Nm = gu_Nm;
	}

	public String getMs_Addr() {
		return ms_Addr;
	}

	public void setMs_Addr(String ms_Addr) {
		this.ms_Addr = ms_Addr;
	}

	public double getMs_Lat() {
		return ms_Lat;
	}

	public void setMs_Lat(double ms_Lat) {
		this.ms_Lat = ms_Lat;
	}

	public double getMs_Lon() {
		return ms_Lon;
	}

	public void setMs_Lon(double ms_Lon) {
		this.ms_Lon = ms_Lon;
	}

	public int getSort_Ord() {
		return sort_Ord;
	}

	public void setSort_Ord(int sort_Ord) {
		this.sort_Ord = sort_Ord;
	}

	public String getCai_Grade() {
		return cai_Grade;
	}

	public void setCai_Grade(String cai_Grade) {
		this.cai_Grade = cai_Grade;
	}

	public int getCai() {
		return cai;
	}

	public void setCai(int cai) {
		this.cai = cai;
	}

	public int getPm25_Conc() {
		return pm25_Conc;
	}

	public void setPm25_Conc(int pm25_Conc) {
		this.pm25_Conc = pm25_Conc;
	}

	public int getPm10_Conc() {
		return pm10_Conc;
	}

	public void setPm10_Conc(int pm10_Conc) {
		this.pm10_Conc = pm10_Conc;
	}

	public double getO3_Conc() {
		return o3_Conc;
	}

	public void setO3_Conc(double o3_Conc) {
		this.o3_Conc = o3_Conc;
	}

	public String getMs_Dt() {
		return ms_Dt;
	}

	public void setMs_Dt(String ms_Dt) {
		this.ms_Dt = ms_Dt;
	}

	public int getCrt_By() {
		return crt_By;
	}

	public void setCrt_By(int crt_By) {
		this.crt_By = crt_By;
	}

	public String getCrt_Dt() {
		return crt_Dt;
	}

	public void setCrt_Dt(String crt_Dt) {
		this.crt_Dt = crt_Dt;
	}

	public int getMod_By() {
		return mod_By;
	}

	public void setMod_By(int mod_By) {
		this.mod_By = mod_By;
	}

	public String getMod_Dt() {
		return mod_Dt;
	}

	public void setMod_Dt(String mod_Dt) {
		this.mod_Dt = mod_Dt;
	}

	@Override
	public int hashCode() {
		return Objects.hash(aq_Id);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Air_QualityVO other = (Air_QualityVO) obj;
		return aq_Id == other.aq_Id;
	}

	@Override
	public String toString() {
		return "Air_QualityVO [aq_Id=" + aq_Id + ", gu_Cd=" + gu_Cd + ", gu_Nm=" + gu_Nm + ", ms_Addr=" + ms_Addr
				+ ", ms_Lat=" + ms_Lat + ", ms_Lon=" + ms_Lon + ", sort_Ord=" + sort_Ord + ", cai_Grade=" + cai_Grade
				+ ", cai=" + cai + ", pm25_Conc=" + pm25_Conc + ", pm10_Conc=" + pm10_Conc + ", o3_Conc=" + o3_Conc
				+ ", ms_Dt=" + ms_Dt + ", crt_By=" + crt_By + ", crt_Dt=" + crt_Dt + ", mod_By=" + mod_By + ", mod_Dt="
				+ mod_Dt + "]";
	}

}
