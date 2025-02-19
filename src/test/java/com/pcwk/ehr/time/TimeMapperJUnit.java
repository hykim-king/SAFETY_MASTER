package com.pcwk.ehr.time;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import com.pcwk.ehr.mapper.TimeMapper;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.mybatis.spring.annotation.MapperScan;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.jupiter.api.Assertions.assertEquals;

@SpringBootTest
@MapperScan(basePackages = "com.pcwk.ehr.mapper")
class TimeMapperJunit {

	final Logger log = LoggerFactory.getLogger(TimeMapperJunit.class);

	@Autowired
	TimeMapper timeMapper;

	@BeforeEach
	void setUp() throws Exception {
		log.info("┌─────────────────────────────────────────────────────────┐");
		log.info("│ setUp()                                                 │");
		log.info("└─────────────────────────────────────────────────────────┘");
	}

	@AfterEach
	void tearDown() throws Exception {
		log.info("┌─────────────────────────────────────────────────────────┐");
		log.info("│ tearDown()                                              │");
		log.info("└─────────────────────────────────────────────────────────┘");
	}

	@Disabled
	@Test
	void beans(){
		log.info("┌─────────────────────────────────────────────────────────┐");
		log.info("│ beans()                                                 │");
		log.info("└─────────────────────────────────────────────────────────┘");

		assert timeMapper != null;
	}

	@Test
	void getNewDateTime(){
		log.info("┌─────────────────────────────────────────────────────────┐");
		log.info("│ getNewDateTime()                                        │");
		log.info("└─────────────────────────────────────────────────────────┘");

		String dateTime = timeMapper.getNewDateTime();
		assertNotNull(dateTime);
	}
}