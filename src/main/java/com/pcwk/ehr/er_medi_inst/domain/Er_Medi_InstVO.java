package com.pcwk.ehr.er_medi_inst.domain;

import java.util.Objects;

public class Er_Medi_InstVO {
	
	private String hpid;
	private String gu_Cd;
	private String duty_Nm;
	private String duty_Addr;
	private String duty_Tel;
	private String er_Tel;
	private int crt_By;
	private String crt_Dt;
	private int mod_By;
	private String mod_Dt;
	
	public Er_Medi_InstVO() {
		super();
	}

	public String getHpid() {
		return hpid;
	}

	public void setHpid(String hpid) {
		this.hpid = hpid;
	}

	public String getGu_Cd() {
		return gu_Cd;
	}

	public void setGu_Cd(String gu_Cd) {
		this.gu_Cd = gu_Cd;
	}

	public String getDuty_Nm() {
		return duty_Nm;
	}

	public void setDuty_Nm(String duty_Nm) {
		this.duty_Nm = duty_Nm;
	}

	public String getDuty_Addr() {
		return duty_Addr;
	}

	public void setDuty_Addr(String duty_Addr) {
		this.duty_Addr = duty_Addr;
	}

	public String getDuty_Tel() {
		return duty_Tel;
	}

	public void setDuty_Tel(String duty_Tel) {
		this.duty_Tel = duty_Tel;
	}

	public String getEr_Tel() {
		return er_Tel;
	}

	public void setEr_Tel(String er_Tel) {
		this.er_Tel = er_Tel;
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
		return Objects.hash(hpid);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Er_Medi_InstVO other = (Er_Medi_InstVO) obj;
		return Objects.equals(hpid, other.hpid);
	}

	@Override
	public String toString() {
		return "Er_Medi_InstVO [hpid=" + hpid + ", gu_Cd=" + gu_Cd + ", duty_Nm=" + duty_Nm + ", duty_Addr=" + duty_Addr
				+ ", duty_Tel=" + duty_Tel + ", er_Tel=" + er_Tel + ", crt_By=" + crt_By + ", crt_Dt=" + crt_Dt
				+ ", mod_By=" + mod_By + ", mod_Dt=" + mod_Dt + "]";
	}
	
	

}
